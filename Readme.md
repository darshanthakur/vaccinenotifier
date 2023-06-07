# COVID-19 Vaccination Slots Notifier

This project aims to enhance the vaccine slot booking experience by providing users with real-time notifications about the availability of COVID-19 vaccination slots. The "COVID-19 Vaccination Slots Notifier" utilizes the officially provided Co-Win API to fetch the vaccine slots' availability, combined with various other APIs for notifying users about the available slots. The tool can be executed in two ways, as described below:

## Features

1. **Display Vaccination Center Details:** This option allows users to view the details of all vaccination centers in a specified district (based on their postal code). The information includes the center name, address, available vaccine types, and slot availability.

2. **Real-time Notification:** Users can opt to receive real-time notifications when vaccines become available in their selected district. Notifications are sent via Telegram group, text message, and email. This feature ensures that users can quickly book their vaccination slots as soon as they become available, increasing the efficiency of the slot booking process.

## Technologies Used

The "COVID-19 Vaccination Slots Notifier" project employs the following technologies:

- **Co-Win API:** The officially provided API by the government of India to fetch COVID-19 vaccination-related data, including center details and slot availability.

- **Telegram API:** Telegram API is used to send real-time notifications to users via Telegram bot.

- **Text Message API (Twilio):** This API enables sending notifications through SMS to users' registered phone numbers.

- **Email API (SendGrid):** An email API is utilized to send notifications to users' email addresses.

