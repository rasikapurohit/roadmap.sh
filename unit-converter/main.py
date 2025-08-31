from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
    

app = FastAPI()

# make cors enabled
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/convert")
def convert_units(category: str, value: float, from_unit: str, to_unit: str):
    # Conversion logic goes here
    match category:
        case "length":
        
            if from_unit == "meters":
                if to_unit == "kilometers":
                    return {"convertedValue": round(value / 1000, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "miles":
                    return {"convertedValue": round(value / 1609.34, 2), "from_unit": from_unit, "to_unit": to_unit}
            elif from_unit == "kilometers":
                if to_unit == "meters":
                    return {"convertedValue": round(value * 1000, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "miles":
                    return {"convertedValue": round(value / 1.60934, 2), "from_unit": from_unit, "to_unit": to_unit}
            elif from_unit == "miles":
                if to_unit == "meters":
                    return {"convertedValue": round(value * 1609.34, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "kilometers":
                    return {"convertedValue": round(value * 1.60934, 2), "from_unit": from_unit, "to_unit": to_unit}
            pass
        case "weight":
            # Weight conversion logic
            if from_unit == "grams":
                if to_unit == "kilograms":
                    return {"convertedValue": round(value / 1000, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "pounds":
                    return {"convertedValue": round(value * 0.00220462, 2), "from_unit": from_unit, "to_unit": to_unit}
            elif from_unit == "kilograms":
                if to_unit == "grams":
                    return {"convertedValue": round(value * 1000, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "pounds":
                    return {"convertedValue": round(value * 2.20462, 2), "from_unit": from_unit, "to_unit": to_unit}
            elif from_unit == "pounds":
                if to_unit == "grams":
                    return {"convertedValue": round(value / 0.00220462, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "kilograms":
                    return {"convertedValue": round(value / 2.20462, 2), "from_unit": from_unit, "to_unit": to_unit}
            pass
        case "temperature":
            # Temperature conversion logic
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    return {"convertedValue": round((value * 9/5) + 32, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "Kelvin":
                    return {"convertedValue": round(value + 273.15, 2), "from_unit": from_unit, "to_unit": to_unit}
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    return {"convertedValue": round((value - 32) * 5/9, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "Kelvin":
                    return {"convertedValue": round((value - 32) * 5/9 + 273.15, 2), "from_unit": from_unit, "to_unit": to_unit}
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    return {"convertedValue": round(value - 273.15, 2), "from_unit": from_unit, "to_unit": to_unit}
                elif to_unit == "Fahrenheit":
                    return {"convertedValue": round((value - 273.15) * 9/5 + 32, 2), "from_unit": from_unit, "to_unit": to_unit}
    return {"category": category, "value": value, "from_unit": from_unit, "to_unit": to_unit, "convertedValue": None}
