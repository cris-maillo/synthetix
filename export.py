import csv
import os
import inspect
import importlib
from typing import Dict, List, Any, Optional

def get_class_attributes(cls) -> List[str]:
    """Extract attribute names from a class's __init__ method"""
    init_signature = inspect.signature(cls.__init__)
    # Skip 'self' parameter and return all other parameter names
    return [param for param in init_signature.parameters.keys() if param != 'self']

def get_object_attributes(obj, attributes: List[str]) -> List[Any]:
    """Extract attributes from an object in the specified order"""
    return [getattr(obj, attr) for attr in attributes]

def get_available_classes() -> Dict[str, type]:
    """Automatically discover all available model classes from the models module"""
    import models
    
    classes = {}
    for name, obj in inspect.getmembers(models):
        # Only include classes (not functions, modules, etc.)
        if inspect.isclass(obj) and obj.__module__ == 'models':
            # Convert class name to entity type (e.g., User -> users, TicketValidation -> validations)
            entity_type = name.lower()
            if entity_type.endswith('validation'):
                entity_type = entity_type.replace('validation', 'validations')
            elif not entity_type.endswith('s'):
                entity_type += 's'
            
            classes[entity_type] = obj
    
    return classes

def export_single_csv(data: List[Any], entity_type: str, output_dir: str, num_examples: int) -> Optional[str]:
    """Export a single CSV file with automatic attribute detection"""
    if not data:
        print(f"Warning: No data found for {entity_type}")
        return None
    
    # Get the class for this entity type
    classes = get_available_classes()
    if entity_type not in classes:
        print(f"Warning: Unknown entity type '{entity_type}'")
        return None
    
    cls = classes[entity_type]
    attributes = get_class_attributes(cls)
    
    # Create filename (pluralize entity type)
    filename = f"{entity_type}.csv"
    filepath = os.path.join(output_dir, filename)
    
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(attributes)
            
            # Write data rows (limited by num_examples)
            for item in data[:num_examples]:
                row_data = get_object_attributes(item, attributes)
                writer.writerow(row_data)
        
        return filename
    except Exception as e:
        print(f"Error exporting {filename}: {e}")
        return None

def export_to_csv(data: Dict[str, List[Any]], num_examples: int = 5, output_dir: str = 'example_data') -> None:
    """
    Export data to CSV files with automatic configuration
    
    Args:
        data: Dictionary containing data lists for each entity type
        num_examples: Number of examples to export per file
        output_dir: Directory to save CSV files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Track successful exports
    successful_exports = []
    failed_exports = []
    
    # Export each data type automatically
    for entity_type, entity_data in data.items():
        result = export_single_csv(entity_data, entity_type, output_dir, num_examples)
        
        if result:
            successful_exports.append(result)
        else:
            failed_exports.append(entity_type)
    
    # Print results
    print(f"\nCSV export completed:")
    print(f"- Output directory: {output_dir}")
    print(f"- Examples per file: {num_examples}")
    
    if successful_exports:
        print(f"\nSuccessfully exported {len(successful_exports)} files:")
        for filename in successful_exports:
            print(f"  - {filename}")
    
    if failed_exports:
        print(f"\nFailed to export {len(failed_exports)} files:")
        for entity_type in failed_exports:
            print(f"  - {entity_type}")
    
    # Print available entity types for reference
    available_classes = get_available_classes()
    print(f"\nAvailable entity types: {', '.join(available_classes.keys())}")