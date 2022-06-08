from tkinter import filedialog

def create_points(Idx, xyzs, coord):
    patran_command = 'STRING asm_create_grid_xyz_created_ids[VIRTUAL]\n'
    patran_command += 'asm_const_grid_xyz( "%s","%s", "%s",asm_create_grid_xyz_created_ids)\n'%(Idx, xyzs, coord)
    
    return patran_command

def create_nodes(Idx, xyzs, coord):
    patran_command = 'STRING fem_create_nodes__nodes_created[VIRTUAL]\n'
    patran_command += 'fem_create_nodes_1( "%s","%s",3,"%s","%s",fem_create_nodes__nodes_created)\n'%(coord, coord, Idx, xyzs )
    
    return patran_command

def create_loadcase(action, lcn, lc, zf, lcf):
    if action == "Create":
        patran_command = 'loadcase_create2( "%s", "Static", "", 1., %s , %s, %s, "", 0., TRUE )\n'%(lcn, lc, zf, lcf)
    elif action == "Modify":
        patran_command = 'loadcase_modify2( "%s", "%s", "Static", "", 1., %s , %s, %s, "", 0., TRUE )\n'%(lcn, lcn, lc, zf, lcf)

    return patran_command

def create_fem_field(action, field_name, EntyType, FieldTyp, cnt, Entity, fld):
    if action == "Create":
        patran_command = 'fields_create_dfem( "%s", "%s", "%s", %d, %s, %s)\n'%(field_name, EntyType, FieldTyp, cnt, Entity, fld)
    elif action == 'Modify':
        patran_command = 'fields_create_dfem( "%s", "%s", "%s", %d, %s, %s)\n'%(field_name, EntyType, FieldTyp, cnt, Entity, fld)
        patran_command = 'fields_modify_dfem( "%s", "%s", "%s", "%s", %d, %s, %s)\n'%(field_name,field_name, EntyType, FieldTyp, cnt, Entity, fld)
        
    patran_command = patran_command.replace("'",'"')
    patran_command = patran_command.replace("None",'')

    return patran_command


def create_load(action, load_type, app_type, EntType, ln, app_reg, cno, sf, F):

    ''' load_type
    CID Distributed Load , Force, Total Load
        app_type
    'Element Uniform' for CID Distributed Load, Total Load
    'Nodal' for Force 
    '''
    if load_type == "Force":
        loads = '["%s", "%s", "%s", "%s"], ["", "", "", ""]'%(F[0], F[1], F[2], F[3])
    elif load_type == "Pressure":
        loads = '["%s", "%s", "%s"], ["", "", ""]'%(F[0], F[1], F[2])        
    elif load_type == "CID Distributed Load":
        loads = '["%s", "%s"], ["", ""]'%(F[0], F[1])
    elif load_type == "Total Load":
        loads = '["%s", "%s"], ["", ""]'%(F[0], F[1])
    
    if action == 'Create':    
        patran_command = 'loadsbcs_create2( "%s", "%s", "%s", "%s", "Static", %s , "FEM", "%s", "%s",'%(ln, load_type, app_type, EntType, app_reg, cno, sf)
    elif action == 'Modify':
        patran_command = 'loadsbcs_modify2( "%s", "%s", "%s", "%s", "%s", "Static", %s , "FEM", "%s", "%s",'%(ln, ln, load_type, app_type, EntType, app_reg, cno, sf)
    
    patran_command += loads +')'

    return patran_command



#def create_elements(oup_id):
#STRING fem_create_elemen_elems_created[VIRTUAL]
#fem_create_elems_1( "Bar" , "Bar2", "9001","Standard", 3,"Node 14797","Node 7420",  "", "", "", "", "", "", fem_create_elemen_elems_created )
#    patran_command = "fem_create_elems_1(%s)" % ",".join([elem_type, topo_type, elem_id, "Standard", 3, node_1, node_2, "fem_create_elemen_elems_created"])
#    return patran_command