import unittest
from os.path import join

import numpy as np
import rasterio
from rasterio.enums import ColorInterp

from rastervision2.core import (RasterStats)
from rastervision2.core.utils.misc import save_img
from rastervision2.core.data import (
    ChannelOrderError, RasterioSourceConfig, StatsTransformerConfig)
from rastervision2.pipeline import rv_config

from tests_v2 import data_file_path


class TestRasterioSource(unittest.TestCase):
    def setUp(self):
        self.tmp_dir_obj = rv_config.get_tmp_dir()
        self.tmp_dir = self.tmp_dir_obj.name

    def tearDown(self):
        self.tmp_dir_obj.cleanup()

    def test_nodata_val(self):
        # make geotiff filled with ones and zeros with nodata == 1
        img_path = join(self.tmp_dir, 'tmp.tif')
        height = 100
        width = 100
        nb_channels = 3
        with rasterio.open(
                img_path,
                'w',
                driver='GTiff',
                height=height,
                width=width,
                count=nb_channels,
                dtype=np.uint8,
                nodata=1) as img_dataset:
            im = np.random.randint(
                0, 2, (height, width, nb_channels)).astype(np.uint8)
            for channel in range(nb_channels):
                img_dataset.write(im[:, :, channel], channel + 1)

        config = RasterioSourceConfig(uris=[img_path])
        source = config.build(tmp_dir=self.tmp_dir)
        with source.activate():
            out_chip = source.get_image_array()
            expected_out_chip = np.zeros((height, width, nb_channels))
            np.testing.assert_equal(out_chip, expected_out_chip)

    def test_mask(self):
        # make geotiff filled with ones and zeros and mask the whole image
        img_path = join(self.tmp_dir, 'tmp.tif')
        height = 100
        width = 100
        nb_channels = 3
        with rasterio.open(
                img_path,
                'w',
                driver='GTiff',
                height=height,
                width=width,
                count=nb_channels,
                dtype=np.uint8) as img_dataset:
            im = np.random.randint(
                0, 2, (height, width, nb_channels)).astype(np.uint8)
            for channel in range(nb_channels):
                img_dataset.write(im[:, :, channel], channel + 1)
            img_dataset.write_mask(
                np.zeros(im.shape[0:2]).astype(np.bool))

        config = RasterioSourceConfig(uris=[img_path])
        source = config.build(tmp_dir=self.tmp_dir)
        with source.activate():
            out_chip = source.get_image_array()
            expected_out_chip = np.zeros((height, width, nb_channels))
            np.testing.assert_equal(out_chip, expected_out_chip)

    def test_get_dtype(self):
        img_path = data_file_path('small-rgb-tile.tif')
        config = RasterioSourceConfig(uris=[img_path])
        source = config.build(tmp_dir=self.tmp_dir)
        self.assertEqual(source.get_dtype(), np.uint8)

    def test_gets_raw_chip(self):
        img_path = data_file_path('small-rgb-tile.tif')
        channel_order = [0, 1]

        config = RasterioSourceConfig(uris=[img_path], channel_order=channel_order)
        source = config.build(tmp_dir=self.tmp_dir)
        with source.activate():
            out_chip = source.get_raw_image_array()
            self.assertEqual(out_chip.shape[2], 3)

    def test_shift_x(self):
        # Specially-engineered image w/ one meter per pixel resolution
        # in the x direction.
        img_path = data_file_path('ones.tif')
        channel_order = [0]

        config = RasterioSourceConfig(
            uris=[img_path], channel_order=channel_order,
            x_shift=1.0, y_shift=0.0)
        source = config.build(tmp_dir=self.tmp_dir)

        with source.activate():
            extent = source.get_extent()
            data = source.get_chip(extent)
            self.assertEqual(data.sum(), 2**16 - 256)
            column = data[:, 255, 0]
            self.assertEqual(column.sum(), 0)

    def test_shift_y(self):
        # Specially-engineered image w/ one meter per pixel resolution
        # in the y direction.
        img_path = data_file_path('ones.tif')
        channel_order = [0]

        config = RasterioSourceConfig(
            uris=[img_path], channel_order=channel_order,
            x_shift=0.0, y_shift=1.0)
        source = config.build(tmp_dir=self.tmp_dir)

        with source.activate():
            extent = source.get_extent()
            data = source.get_chip(extent)
            self.assertEqual(data.sum(), 2**16 - 256)
            row = data[0, :, 0]
            self.assertEqual(row.sum(), 0)

    def test_gets_raw_chip_from_uint16_transformed_proto(self):
        img_path = data_file_path('small-uint16-tile.tif')
        channel_order = [0, 1]

        config = RasterioSourceConfig(uris=[img_path])
        raw_rs = config.build(tmp_dir=self.tmp_dir)

        stats_uri = join(self.tmp_dir, 'tmp.tif')
        stats = RasterStats()
        stats.compute([raw_rs])
        stats.save(stats_uri)

        transformer = StatsTransformerConfig(stats_uri=stats_uri)
        config = RasterioSourceConfig(
            uris=[img_path],
            channel_order=channel_order,
            transformers=[transformer])
        rs = config.build(tmp_dir=self.tmp_dir)

        with rs.activate():
            out_chip = rs.get_raw_image_array()
            self.assertEqual(out_chip.shape[2], 3)

    def test_uses_channel_order(self):
        img_path = join(self.tmp_dir, 'img.tif')
        chip = np.ones((2, 2, 4)).astype(np.uint8)
        chip[:, :, :] *= np.array([0, 1, 2, 3]).astype(np.uint8)
        save_img(chip, img_path)

        channel_order = [0, 1, 2]
        config = RasterioSourceConfig(
            uris=[img_path], channel_order=channel_order)
        source = config.build(tmp_dir=self.tmp_dir)

        with source.activate():
            out_chip = source.get_image_array()
            expected_out_chip = np.ones((2, 2, 3)).astype(np.uint8)
            expected_out_chip[:, :, :] *= np.array([0, 1,
                                                    2]).astype(np.uint8)
            np.testing.assert_equal(out_chip, expected_out_chip)

    def test_channel_order_error(self):
        img_path = join(self.tmp_dir, 'img.tif')
        chip = np.ones((2, 2, 3)).astype(np.uint8)
        chip[:, :, :] *= np.array([0, 1, 2]).astype(np.uint8)
        save_img(chip, img_path)

        channel_order = [3, 1, 0]
        with self.assertRaises(ChannelOrderError):
            config = RasterioSourceConfig(
                uris=[img_path], channel_order=channel_order)
            config.build(tmp_dir=self.tmp_dir)

    def test_detects_alpha(self):
        # Set first channel to alpha. Expectation is that when omitting channel_order,
        # only the second and third channels will be in output.
        img_path = join(self.tmp_dir, 'img.tif')
        chip = np.ones((2, 2, 3)).astype(np.uint8)
        chip[:, :, :] *= np.array([0, 1, 2]).astype(np.uint8)
        save_img(chip, img_path)

        ci = (ColorInterp.alpha, ColorInterp.blue, ColorInterp.green)
        with rasterio.open(img_path, 'r+') as src:
            src.colorinterp = ci

        config = RasterioSourceConfig(uris=[img_path])
        source = config.build(tmp_dir=self.tmp_dir)
        with source.activate():
            out_chip = source.get_image_array()
            expected_out_chip = np.ones((2, 2, 2)).astype(np.uint8)
            expected_out_chip[:, :, :] *= np.array([1, 2]).astype(np.uint8)
            np.testing.assert_equal(out_chip, expected_out_chip)

    def test_non_geo(self):
        # Check if non-georeferenced image files can be read and CRSTransformer
        # implements the identity function.
        img_path = join(self.tmp_dir, 'img.png')
        chip = np.ones((2, 2, 3)).astype(np.uint8)
        save_img(chip, img_path)

        config = RasterioSourceConfig(uris=[img_path])
        source = config.build(tmp_dir=self.tmp_dir)
        with source.activate():
            out_chip = source.get_image_array()
            np.testing.assert_equal(out_chip, chip)

            p = (3, 4)
            out_p = source.get_crs_transformer().map_to_pixel(p)
            np.testing.assert_equal(out_p, p)

            out_p = source.get_crs_transformer().pixel_to_map(p)
            np.testing.assert_equal(out_p, p)

    def test_no_epsg(self):
        crs = rasterio.crs.CRS()
        img_path = join(self.tmp_dir, 'tmp.tif')
        height = 100
        width = 100
        nb_channels = 3
        with rasterio.open(
                img_path,
                'w',
                driver='GTiff',
                height=height,
                width=width,
                count=nb_channels,
                dtype=np.uint8,
                crs=crs) as img_dataset:
            im = np.zeros((height, width, nb_channels)).astype(np.uint8)
            for channel in range(nb_channels):
                img_dataset.write(im[:, :, channel], channel + 1)

        try:
            config = RasterioSourceConfig(uris=[img_path])
            config.build(tmp_dir=self.tmp_dir)
        except Exception:
            self.fail(
                'Creating RasterioSource with CRS with no EPSG attribute '
                'raised an exception when it should not have.')


if __name__ == '__main__':
    unittest.main()
