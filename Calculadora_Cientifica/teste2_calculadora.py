import pytest
from calculadora import Calculadora_cientifica

x = Calculadora_cientifica()

def test_validar():
    assert x._validar(4,1) == True
    assert x._validar(4) == True
    assert x._validar(-10,1) == True
    assert x._validar(10,2.5) == True
    with pytest.raises(TypeError):
        x._validar(1,"1")
        x._validar("1","1")
        x._validar("1",1)

def test_soma():
    assert x.soma(4,1) == 5
    assert x.soma(4,0) != 5
    assert x.soma(10,-1) == 9
    with pytest.raises(TypeError):
        x.soma(1,"1")
        x.soma("1","1")
        x.soma("1",1)

def test_subtracao():
    assert x.subtracao(15,10) == 5
    assert x.subtracao(15,8) != 5
    assert x.subtracao(10,-10) == 20
    assert x.subtracao(-15,10) == -25
    with pytest.raises(TypeError):
        x.subtracao(1,"1")
        x.subtracao("1","1")
        x.subtracao("1",1)

def test_multiplicacao():
    assert x.multiplicacao(10,5) == 50
    assert x.multiplicacao(5,5) == 25
    assert x.multiplicacao(10,10) != 20
    assert type(x.multiplicacao(15,10)) == int
    with pytest.raises(TypeError):
        x.multiplicacao(1,"1")
        x.multiplicacao("1","1")
        x.multiplicacao("1",1)

def test_divisao():
    assert x.divisao(10,5) == 2
    assert x.divisao(5,5) == 1
    assert x.divisao(10,10) != 2
    assert type(x.divisao(15,10)) == float
    with pytest.raises(TypeError):
        x.divisao(1,"1")
        x.divisao("1","1")
        x.divisao("1",1)
    with pytest.raises(ZeroDivisionError):
        x.divisao(42,0)
        x.divisao(10,0)
        x.divisao(0,0)

def test_potenciacao():
    assert x.potenciacao(10,2) == 100
    assert x.potenciacao(0,3) == 0
    assert x.potenciacao(3,0) == 1
    assert type(x.potenciacao(15,10)) == float
    with pytest.raises(TypeError):
        x.potenciacao("x","y")
        x.potenciacao(4,"y")
        x.potenciacao("x",4)