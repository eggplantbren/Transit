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

#ifndef _TransitModel_
#define _TransitModel_

#include "Model.h"
#include <vector>

class TransitModel:public DNest3::Model
{
	private:
		/*
		* ALL PARAMETERS ARE LATENT VARIABLES WITH U(0, 1) PRIOR
		* THESE GET TRANSFORMED PRIOR TO LIKELIHOOD EVALUATION
		*/

		// Transit parameters
		double _amplitude, _period, _width, _offset, _smooth;

		// Noise standard deviation
		double _sigma;

		// Actual parameters
		double amplitude, period, width, offset, smooth;
		double sigma;
		// Compute them from the latent parameters
		void assemble();

		double perturbOne();
		double& chooseParam();

	public:
		TransitModel();

		// Generate the point from the prior
		void fromPrior();

		// Metropolis-Hastings proposals
		double perturb();

		// Stretch moves
		//double perturb_stretch(const TransitModel& other, double Z);

		// Likelihood function
		double logLikelihood() const;

		// Print to stream
		void print(std::ostream& out) const;

		// Return string with column information
		std::string description() const;
};

#endif

