# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:08:31 2025

@author: Aisha Arfan
"""


import ifcopenshell



print("ifcopenshell version:", ifcopenshell.version)


# Open IFC file
ifc_file = ifcopenshell.open("25-16-D-STR (2).ifc")
print("Filen er åbnet:", ifc_file.schema)

## BEAMS ##
beams = ifc_file.by_type("IfcBeam")

for beam in beams:
    print("Beam:", beam.Name)

    # Check property sets
    for definition in beam.IsDefinedBy:
        if definition.is_a("IfcRelDefinesByProperties"):
            property_set = definition.RelatingPropertyDefinition
            print("  Property set:", property_set.Name)

    # Check material
    for rel in beam.HasAssociations:
        if rel.is_a("IfcRelAssociatesMaterial"):
            print("  Material:", rel.RelatingMaterial.Name)
            


        


