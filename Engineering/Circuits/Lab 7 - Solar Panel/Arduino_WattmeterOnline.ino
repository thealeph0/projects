/*
 * Sketch written for Arduino Uno to solar panel voltage and power
 * Marnie Wong May 2021 
 * Uses an Operational Amplifer powered from the Arduino to measure the voltage
 * which is then read on Analog input A0 and displayed on the Serial monitor
*/
 
const long Rf = ; //enter value of feedback resistor in Ohms
const long Ri = ; //enter value of bias resistor in Ohms
const long R1 = ; //enter value of series resistor in Ohms
const long R2 = ; //enter value of load resistor in Ohms
const long Rsh = 5; //enter value of shunt resistor in Ohms
float Read_Vtemp = A1;//value read from ADC on pin A1
float Read_Itemp  = A0;//value read from ADC on pin A0
float Gain; //Gain of the Op-Amp Circuit
float Vtemp; //setting temporary analog voltage input
float Itemp; //setting temporary analog current input (actually a voltage reading)
float Voltage = 0.0; //initializing voltage reading
float Current = 0.0; //initializing current reading
float Power = 0.0;   //initializing power calculation

void setup() 
{
  Serial.begin(9600); //set up serial monitor

}

void loop() 
{
 
 Vtemp = analogRead(Read_Vtemp);
 Itemp = analogRead(Read_Itemp);

 // Voltage Measurement
 // 1. Converts the analog input (max 5V) into a digital value (max 1024)
 // 2. Accounts for the voltage divider calculation
 Voltage = Vtemp * (5.0/1024.0) * (R1+R2) / R2; //in Volts
 
 // Current Measurement
 // 1. Calculates the Op-Amp Gain
 Gain = 1+(Rf/Ri); //in V/V
 // 2. Converts the analog input (5V max) into a digital value (max 1024)
 // 3. Accounts for the op-amp gain, current to voltage conversion (Rsh), and units (mA=1/1000)
 Current = Itemp*(5.0/1024.0)/(Gain*Rsh)*1000; //in mA
 
 
 // Power Measurement
 Power = Voltage * Current;//Calculation of power from solar panel in mW

 // Print values to the serial monitor for verification
 Serial.print("ADCV reads: ");
 Serial.print(Vtemp);
 Serial.print("   Solar Panel Voltage is: ");
 Serial.print(Voltage);
 Serial.print(" Volts");
 Serial.println("");
 Serial.println("  ");
 delay(1000); 
  
 Serial.print("ADCI reads: ");
 Serial.print(Itemp);
 Serial.print("   Solar Panel Current is: ");
 Serial.print(Current);
 Serial.print(" milliAmps");
 Serial.println("");
 Serial.println("  ");
 delay(1000); 
  
 Serial.print("Solar Panel Power is: ");
 Serial.print(Power);
 Serial.print(" milliWatts");
 Serial.println("  ");
 Serial.println("__________________");
 delay(1000); 
 
}



  
