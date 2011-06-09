// This file is part of Man, a robotic perception, locomotion, and
// team strategy application created by the Northern Bites RoboCup
// team of Bowdoin College in Brunswick, Maine, for the Aldebaran
// Nao robot.
//
// Man is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Man is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser Public License for more details.
//
// You should have received a copy of the GNU General Public License
// and the GNU Lesser Public License along with Man.  If not, see
// <http://www.gnu.org/licenses/>.

/**
 * This class links a NoiseMeter and SignalMonitor together to provide
 * a first-warning system for failed sensors. Also, it provides a way
 * to quantify the amount of noise present in our data under game
 * circumstances. At destruction, this class will log the data it has
 * collected to /tmp/sensorName.xls
 *
 * Currently this class doesn't do any filtering of the data, but that
 * would be trivial to template and add (currently using a width 1 Boxcar).
 *
 * @see dsp.h
 * @author Nathan Merritt
 * @date June 2011
 */

#pragma once
#ifndef SENSOR_MONITOR_H
#define SENSOR_MONITOR_H

#include "dsp.h"

#include <string>

#define NOT_STEADY -1

static const int numberOfBins = 25;

class SensorMonitor : public Filter
{
public:
	SensorMonitor(std::string sensorName, double low, double high, bool log=false);
	~SensorMonitor();

	double X(double);
	void Reset();
	void LogOutput(); 	// prints histograms to /tmp/{sensorName}.sensor

private:
	std::string sensorName;
	NoiseMeter<Butterworth> noise;
	SignalMonitor monitor;
	int steadyAtFrame;
};


#endif
