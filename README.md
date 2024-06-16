## Body Mass Index(BMI) Calculator

The BMI calculator interface consists of fields for the user to enter their age, height, and weight. Additionally, users can specify their gender using radio buttons. Once the required information is provided, users can calculate their BMI and receive feedback based on their BMI category. The interface also includes buttons to clear inputs and exit the application.

**Layout and Design**
The main window is configured with a title, specific dimensions, and a light blue background. The fonts used for labels and buttons are specified for consistency and readability.

## Components

**Title Label:**

 - Displays "BMI CALCULATOR" at the top of the window.

**Gender Selection:**

 - Two radio buttons allow the user to select their gender (Male or Female).

**Input Fields:**

 - Age: Entry widget for the user to input their age.
 - Height: Entry widget for the user to input their height in centimeters.
 - Weight: Entry widget for the user to input their weight in kilograms.

**Buttons:**

 - Calculate: Triggers the BMI calculation based on the entered data.
 - Clear: Clears all input fields and the BMI result.
 - Exit: Closes the application.
    
**BMI Result Label:**

 - Displays the calculated BMI and corresponding remarks based on the BMI category.

**Functionality**
 - Age Validation: Ensures the entered age is a positive integer between 0 and 120.
 - Height Validation: Ensures the entered height is a positive number.
 - Weight Validation: Ensures the entered weight is a positive number.
 - Calculate BMI: Uses the formula 
         **BMI = weight (kg) / height^2 (m^2)​**
  to compute the BMI and provides a categorized remark.

 - Clear Inputs: Resets all input fields and the result display.
 - Exit Application: Closes the application window.

## Error Handling

 - The script includes robust error handling to ensure that users enter valid data:

 - If the age, height, or weight fields are empty or contain invalid characters, an error message is displayed.
Specific error messages guide the user to correct their input.

 ## Conclusion
This BMI calculator provides a simple and effective way to calculate and understand BMI. The interface is intuitive, ensuring that users can easily input data and interpret results. The error handling ensures that the inputs are valid, thereby preventing incorrect calculations and providing a smooth user experience.

## Output


![Screenshot 2024-06-16 211115](https://github.com/Pratham3642/BMI-Calculator/assets/162919475/d86ba52b-46b3-4c6a-a455-e1dbb6a1a272)





