"""Functional tests using the API with a fake Apple TV."""

import asyncio

from aiohttp import web
from aiohttp.test_utils import (AioHTTPTestCase, unittest_run_loop)

from pyatv import (connect_to_apple_tv, const, exceptions)
from pyatv.conf import (AirPlayService, MrpService, AppleTV)

from tests import (utils, zeroconf_stub, common_functional_tests)
from tests.mrp.fake_mrp_atv import (
    FakeAppleTV, AppleTVUseCases)


class MRPFunctionalTest(common_functional_tests.CommonFunctionalTests):

    def setUp(self):
        super().setUp()
        self.atv = self.get_connected_device(self.fake_atv.port)

    def tearDown(self):
        pass

    @asyncio.coroutine
    def get_application(self, loop=None):
        self.fake_atv = FakeAppleTV(self)
        self.usecase = AppleTVUseCases(self.fake_atv)
        yield from self.fake_atv.start(self.loop)
        return self.fake_atv

    def get_connected_device(self, port):
        conf = AppleTV('127.0.0.1', 'Test device')
        conf.add_service(MrpService(port))
        conf.add_service(AirPlayService(self.server.port))
        return connect_to_apple_tv(conf, loop=self.loop)

    @unittest_run_loop
    def test_dummy_test(self):
        self.assertFalse(True)
