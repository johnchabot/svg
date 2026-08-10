import xml.etree.ElementTree as ET

def evaluate_modulo6_helix(parent_facet, shift_amount):
    """Calculates the 1-to-6 indexed orientation shift."""
    return ((parent_facet + shift_amount - 1) % 6) + 1

def calculate_linear_density(length, interval, min_c, max_c):
    """Computes generation counts based on parent component length."""
    computed = int(length // interval)
    return max(min_c, min(max_c, computed))

# Simulated Runtime Initialization
if __name__ == "__main__":
    xml_data = """<plant id="pelargonium-specimen" genus="Pelargonium">
        <generation-rules>
            <rule target="facet-orientation-shifts">
                <param name="axial-step" value="2"/>
                <param name="inflorescence-offset" value="4"/>
            </rule>
            <rule target="inflorescence-umbel">
                <param name="spacing-interval" value="12"/>
            </rule>
        </generation-rules>
    </plant>"""
    
    root = ET.fromstring(xml_data)
    axial_step = int(root.find(".//param[@name='axial-step']").attrib['value'])
    spacing_int = float(root.find(".//param[@name='spacing-interval']").attrib['value'])
    
    # Process Tier 1 Cascade Transformation Matrix
    parent_tier_facet = 1
    child_tier_facet = evaluate_modulo6_helix(parent_tier_facet, axial_step)
    
    # Process Dynamic Linear Component Count
    stalk_length = 180.0
    generated_flowers = calculate_linear_density(stalk_length, spacing_int, 3, 24)
    
    print(f"--- FLORA PROCESSING INTERFACE RUNTIME ---")
    print(f"Parent Stem Facet Index : {parent_tier_facet}")
    print(f"Computed Child Stem Facet (Helix Step +{axial_step}): {child_tier_facet}")
    print(f"Stalk Length Verified   : {stalk_length}mm")
    print(f"Generated Subcomponents : {generated_flowers} Flower Units instantiated.")
