# devicesportfolio
This project is a modular suite of Python tools for connecting, automating, and managing diverse warehouse and industrial devices — from barcode scanners, cameras, and weight sensors, to PLC systems, FTP, and mail services.

Each integration is a standalone Python module, designed to be reusable and easy to plug into larger automation or control systems.


✅ Key Capabilities

📦 Automates barcode reading from hand scanners, cameras, and industrial scanners (Cognex).

📸 Captures images and dimensions from cameras (Hikvision, Dahua, Logitech).

⚖️ Reads weights and dimensions from sensors using Modbus, TCP, and OPC-UA.

📂 Connects to FTP servers to transfer data automatically.

📬 Sends data and reports via email.

📑 Automates barcode printing with TSC printers.

🌐 Uses Selenium to fetch data from web apps like Chrome/WhatsApp.

🚦 Controls machinery and carriages by sending commands.



| Module                  | Purpose                                                      |
| ----------------------- | ------------------------------------------------------------ |
| **audiotest**           | Detects audio input; triggers actions (e.g., open WhatsApp). |
| **barcode**             | Reads barcodes from handheld scanners via COM port.          |
| **barcodecognex**       | Fetches barcode data from Cognex scanners.                   |
| **camerabarcode**       | Detects barcodes using live camera feed.                     |
| **chrome**              | Uses Selenium to automate Chrome tasks and scrape data.      |
| **dahuadim**            | Gets product dimensions using a Dahua camera.                |
| **Detectbarcode**       | Uses pyzbar to decode barcodes from images/video.            |
| **dimcognexcamera**     | Fetches dimensions from Cognex smart cameras.                |
| **dimmodbus**           | Reads dimensions from sensors over Modbus (COM port).        |
| **FTP**                 | Connects to FTP servers and transfers files.                 |
| **hikvisiontest**       | Connects to a Hikvision camera and saves images.             |
| **logitech**            | Connects to a Logitech webcam and saves images.              |
| **mail**                | Sends data/reports via email (e.g., SMTP).                   |
| **Multibarcodeprinter** | Uses TSC printer and CSV to print barcodes in bulk.          |
| **opcua**               | Reads PLC DB data using OPC-UA protocol.                     |
| **runner**              | Sends commands to move carriages/machinery.                  |
| **weightmodbus**        | Reads weight data from Modbus-connected scales.              |
| **weighttcp**           | Reads weight data from TCP/IP-connected scales.              |

