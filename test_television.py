import pytest
from television import Television

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv.power()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 1"
        self.tv.mute()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        self.tv.channel_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"
        for _ in range(3):
            self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.tv.channel_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 3, Volume = 0"
        for _ in range(3):
            self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

    def test_volume_up(self):
        self.tv.volume_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
        self.tv.mute()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"
        for _ in range(3):
            self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        self.tv.volume_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
        self.tv.mute()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        for _ in range(3):
            self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", "-s",__file__])
