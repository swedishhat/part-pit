
Parameters
----------
Parameters specify the electrical and mechanical properties of the component. They can be almost anything,
but you should try to align them with an existing component schema for the sake of library consistency and 
part searchability. 

Parameters are always of the form:

[parameter.name]
value = <string> or <number> 
unit = <string> 
visible = <boolean> 


#[[parameter]]
#name = "temp_min"
#value = -55.0
#unit = "C"

# [[parameter]]
# name = "temp_max"
# value = 155.0
# unit = "C"

# [[parameter]]
# name = "temp_coeff"
# value = 50.0
# unit = "ppm/C"

# [[parameter]]
# name = "length"
# value = 1.0
# unit = "mm"

# [[parameter]]
# name = "width"
# value = 0.5
# unit = "mm"

# [[parameter]]
# name = "height"
# value = 0.4
# unit = "mm"

# [[supplierlink]]
# manufacturer = ""
# mpn = ""
# supplier = ""
# spn = ""

