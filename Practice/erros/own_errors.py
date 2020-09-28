class MyCustomError(TypeError):
    pass


raise MyCustomError('Ouch! An error happend.')


