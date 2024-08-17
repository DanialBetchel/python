class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Init the TV with defaults.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        self.__previous_volume: int = self.__volume

    def power(self) -> None:
        """
        Toggle TV power.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle mute.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__previous_volume
                self.__muted = False
            else:
                self.__previous_volume = self.__volume
                self.__volume = self.MIN_VOLUME
                self.__muted = True

    def channel_up(self) -> None:
        """
        Go up a channel.
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Go down a channel.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Turn volume up.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Turn volume down.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return TV state.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
