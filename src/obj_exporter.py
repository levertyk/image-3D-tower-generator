import trimesh

def export_to_obj(towers, output_file):
    mesh = trimesh.Trimesh(vertices=[], faces=[])
    for tower in towers:
        #TODO convert tower to mesh and add to mesh
        pass
    mesh.export(output_file)
