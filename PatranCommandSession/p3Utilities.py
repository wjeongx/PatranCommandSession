def line_breaking(xLine):

    icol = 96
    Session = ""
    while xLine != "":
        print("xline = %s"%xLine)
        if len(xLine) > icol :
            Session += xLine[:icol] + "@\n"
        else:
            Session += xLine[:icol] + "\n"
            
        xLine = xLine[icol:]

    return Session



#def create_elements(oup_id):
#STRING fem_create_elemen_elems_created[VIRTUAL]
#fem_create_elems_1( "Bar" , "Bar2", "9001","Standard", 3,"Node 14797","Node 7420",  "", "", "", "", "", "", fem_create_elemen_elems_created )
#    patran_command = "fem_create_elems_1(%s)" % ",".join([elem_type, topo_type, elem_id, "Standard", 3, node_1, node_2, "fem_create_elemen_elems_created"])
#    return patran_command