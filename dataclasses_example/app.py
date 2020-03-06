from dataclasses_example.user import User

u = User('jc', 'test')
u2 = User('jc', 'test')

print(u)
print(u2)
print(u == u2)