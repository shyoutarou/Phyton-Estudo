try:

    f = open("pagina.html", "w", encoding="utf-8")
    ##  f.write("Lorum Ipsum")

    s = "ABCDE"
    s[16]

    raise TypeError("Only integers are allowed")
    raise ValueError("Only integers are allowed")
##  s["anarelo", "vernelho", "verde"]
##  s["narrom"]

##  float(35,4)

##  int("abc")

##  while x < 0:
##    print(x)
##    x = x + 1

##  mensalidades = {"carro": 500, "casa": 1500}
##  print(mensalidades["seguro"])

##  x = 0
##  while x < 10:
##    print(x)
##   x = x + 1
##
##  a = 10
##  for e in [1,2,3]
##  a = "5

except SyntaxError:
    print("SyntaxError")
except IndentationError:
    print("IdentationError")
except KeyError:
    print("KeyError")
except NameError:
    print("NameError")
except ValueError:
    print("ValueError ")
except TypeError:
    print("TypeError ")
except IndexError:
    raise ValueError("Only integers are allowed")
    print("IndexError ")

except ZeroDivisionError as detail:
    print("Handling run-time ZeroDivisionError error:", detail)
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly
    x, y = inst.args
    print("x =", x)
    print("y =", y)
except IOError:
    print("cannot open", arg)
except (RuntimeError, TypeError, NameError):
    print("cannot open", arg)  # handle multiple exceptions
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()


