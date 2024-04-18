from typing import Optional



class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    
    def __init__(self) -> None:
        """
        Initializes a Television object with default values.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the television.
        """
        if not self.__status:
            return
        self.__muted = not self.__muted


    def channel_up(self) -> None:
        """
        Increases the channel of the television by 1.
        If the maximum channel is reached, it wraps around to the minimum channel.
        """
        if not self.__status:
            return
        if self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel of the television by 1.
        If the minimum channel is reached, it wraps around to the maximum channel.
        """
        if not self.__status:
            return
        if self.__channel > Television.MIN_CHANNEL:
            self.__channel -= 1
        else:
            self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self) -> None:
        """
        Increases the volume of the television by 1.
        If the maximum volume is reached, it does not change the volume.
        """
        if not self.__status:
            return
        self.__muted = False
        if self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume of the television by 1.
        If the minimum volume is reached, it does not change the volume.
        """
        if not self.__status:
            return
        self.__muted = False
        if self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1
    
    def __str__(self) -> str:
        """
        Returns a string representation of the Television object.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME if self.__muted else self.__volume}"