from abc import ABCMeta, abstractmethod

# ------产品------
class Player:
    def __init__(self, face=None, body=None, arms=None, legs=None):
        self.face = face
        self.body = body
        self.arms = arms
        self.legs = legs

    def __str__(self):
        return '%s,%s,%s,%s' % (self.face, self.body, self.arms, self.legs)

# ------抽象建造者------
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arms(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass

# ------具体建造者,隐藏了一个产品的内部结构------
class GirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '漂亮的脸蛋'

    def build_body(self):
        self.player.body = '苗条的身材'

    def build_arms(self):
        self.player.arms = '细细的胳膊'

    def build_legs(self):
        self.player.legs = '大长腿'

# ------具体建造者，表示代码------
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '绿脸'

    def build_body(self):
        self.player.body = '魁梧的身体'

    def build_arms(self):
        self.player.arms = '粗壮的胳膊'

    def build_legs(self):
        self.player.legs = '粗壮的大腿'

# ------指挥者，构造代码(构造代码和表示代码分开)，可以对构造过程进行更加精细地控制------
class PlayerDirectory():
    def builder_player(self, builder):
        """
        隐藏了装配过程
        :param builder:
        :return:
        """
        builder.build_face()
        builder.build_body()
        builder.build_arms()
        builder.build_legs()
        return builder.player

# ------客户端------
builder = GirlBuilder()
director = PlayerDirectory()
p = director.builder_player(builder)
print(p)  # 漂亮的脸蛋,苗条的身材,细细的胳膊,大长腿