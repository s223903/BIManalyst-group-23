# BIManalyst group xy
# A1 Submission

## 1) Group number
Group **23**

## 2) Focus area
**Structure**

## 3) Claim being checked
Beams in the IFC model contain property sets and associated materials that can be extracted programmatically.

## 4) Report / Source
- Report: IFC4X3 Documentation / Model schema
- Section: IfcBeam, IsDefinedBy, HasAssociations
- Page/Section: Relevant property definition section

## 5) Description of the script

### For analysts
The script:
- Opens an IFC file.
- Finds all beams (`IfcBeam`) in the model.
- Extracts property sets (`IsDefinedBy → IfcRelDefinesByProperties`).
- Extracts materials (`HasAssociations → IfcRelAssociatesMaterial`).
- Prints beam names, property set names, and material names.
- # Open IFC file
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
