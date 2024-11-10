import os

print(__file__)
print(os.path.realpath('./game.py'))
print(os.path.realpath('../data/records.csv'))
print(os.path.dirname(__file__))
print(
    os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__)))
)

print(
    os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.realpath(__file__)
            )
        )
        , 'data', 'records.csv'
    )
)