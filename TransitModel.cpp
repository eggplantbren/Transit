/*
* Copyright (c) 2009, 2010, 2011, 2012 Brendon J. Brewer.
*
* This file is part of DNest3.
*
* DNest3 is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* DNest3 is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with DNest3. If not, see <http://www.gnu.org/licenses/>.
*/

#include "TransitModel.h"
#include "RandomNumberGenerator.h"
#include "Utils.h"
#include <cmath>

using namespace std;
using namespace DNest3;

TransitModel::TransitModel()
{

}

void TransitModel::fromPrior()
{
	_amplitude	= randomU();
	_period		= randomU();
	_width		= randomU();
	_offset		= randomU();
	_smooth		= randomU();
	_sigma		= randomU();
	assemble();
}

double& TransitModel::chooseParam()
{
	int which = randInt(6);
	if(which == 0)
		return _amplitude;
	else if(which == 1)
		return _period;
	else if(which == 2)
		return _width;
	else if(which == 3)
		return _offset;
	else if(which == 4)
		return _smooth;
	else if(which == 5)
		return _sigma;
	return _amplitude;
}

double TransitModel::perturbOne()
{
	double& param = chooseParam();
	param += pow(10., 1.5 - 6.*randomU());
	param = mod(param, 1.);
	return 0.;
}

void TransitModel::assemble()
{
	amplitude = exp(log(1E-3) + log(1E6)*_amplitude);
	period = exp(log(1.) + log(1E6)*_period);
	width  = exp(log(1E-6) + log(1E6)*_width);
	offset = _offset;
	smooth = exp(log(1E-4) + log(1E4)*_smooth);
	sigma  = exp(log(1E-3) + log(1E6)*_sigma);
}

double TransitModel::perturb()
{
	double logH = 0.;

	int num = 1. + randInt(6);
	for(int i=0; i<num; i++)
		logH += perturbOne();

	assemble();
	return logH;
}

double TransitModel::logLikelihood() const
{
	return 0.;
}

void TransitModel::print(std::ostream& out) const
{
	out<<amplitude<<' '<<period<<' '<<width<<' '<<offset<<' '<<smooth<<' '<<sigma<<' ';
}

string TransitModel::description() const
{
	return string("# amplitude, period, width, offset, smooth, sigma");
}


double TransitModel::logistic(double x, double scale)
{
	return 1./(1. + exp(-x/scale));
}

double TransitModel::transit_shape(double tt, double smooth)
{
	return logistic(abs(tt) - 0.5, smooth) - 1.;
}

double TransitModel::transit(double t, double amplitude, double period,
				double width, double offset, double smooth)
{
	double phase = mod(t/period - offset - 0.5, 1.) - 0.5;
	return amplitude*transit_shape(phase/width, smooth);
}

