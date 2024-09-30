# Smart Parking System

## Overview

The Slot Booking API is a lightweight web service built with Flask that allows users to log and retrieve booked slot information. This API is designed for applications like appointment scheduling systems or event booking platforms, where users can select and confirm specific time slots.

## Key Features

- **Log Button ID**: Users can send a POST request to log the selected slot via a button ID.
- **Get Booked Slot**: Users can retrieve the currently booked slot through a simple GET request.
- **CORS Support**: The API supports Cross-Origin Resource Sharing (CORS), enabling access from different domains.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **Flask-CORS**: An extension that enables CORS, allowing API access from various domains.

## API Endpoints

1. **POST /log_button_id**
   - Logs the ID of the clicked button (booked slot).
   - **Request Body**: JSON object containing the `button_id`.
   - **Response**: Returns the logged `button_id` or an error message if the input is invalid.

   **Example Request**:
   ```json
   {
       "button_id": "desired_slot_id"
   }
