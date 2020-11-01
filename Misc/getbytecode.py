import dis
code = compile(open('hello.py').read(), '', 'exec')
dis.dis(code)
