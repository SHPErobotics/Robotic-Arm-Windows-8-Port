using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO.Ports;

namespace Robotic_Arm___WindowsFormsApplication
{
    class serialCom
    {
        public serialCom()
        {
            comPort = new SerialPort();
            portNames = SerialPort.GetPortNames();
        }

        public serialCom(string n, int b)
        {
            comPort = new SerialPort(n, b);
        }

        public string[] avaiPorts()
        {
            return portNames;
        }

        public string[] avaiBaudRates()
        {
            return baudRates;
        }

        public void setComPort(string n)
        {
            comPort.PortName = n;
        }

        public void setBaud(string n)
        {
            comPort.BaudRate = int.Parse(n);
        }

        public bool openPort()
        {
            comPort.Open();

            return comPort.IsOpen;
        }

        public void write(string n)
        {
            comPort.WriteLine(n);
        }


        public SerialPort comPort;
        private string[] portNames;
        private string[] baudRates = { "300", "600,", "1200", "2400", "9600", "14400", "19200", "38400", "57600", "115200" };

    }
}
