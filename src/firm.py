#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)
Paweł Fiedor (pawel@fiedor.eu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from abm_template.src.baseagent import BaseAgent

# ============================================================================
#
# class Firm
#
# ============================================================================


class Firm(BaseAgent):
    #
    #
    # VARIABLES
    #
    #
    identifier = ""
    parameters = {}
    state_variables = {}
    accounts = []  # all accounts of a bank

    parameters["rl"] = 0.0  # interest rate on loans
    parameters["min_investments"] = 0.0  # minimum loan demand every step
    parameters["max_investments"] = 0.0  # maximum loan demand every step
    parameters["active"] = 0

#
#
# CODE
#
#

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        super(Firm, self).set_identifier(_value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, _value):
        """
        Class variables: parameters
        Local variables: _params
        """
        super(Firm, self).set_parameters(_value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _value):
        """
        Class variables: state_variables
        Local variables: _variables
        """
        super(Firm, self).set_state_variables(_value)

    # -------------------------------------------------------------------------
    # functions needed to make Firm() hashable
    # -------------------------------------------------------------------------
    def __key__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__key__() == other.__key__()

    def __hash__(self):
        return hash(self.__key__())
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self):
        self.accounts = []  # clear transactions when firm is initialized
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __del__
    # -------------------------------------------------------------------------
    def __del__(self):
        pass
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # __str__
    # -------------------------------------------------------------------------
    def __str__(self):
        text = "<firm identifier='" + self.identifier + "'>\n"
        text += "    <value name='active' value='" + str(self.parameters["active"]) + "'></value>\n"
        text += "    <parameter type='changing' name='rl' value='" + str(self.parameters["rl"]) + "'></parameter>\n"
        text += "    <parameter name='min_investments' value='" + str(self.parameters["min_investments"]) + "'></parameter>\n"
        text += "    <parameter name='max_investments' value='" + str(self.parameters["max_investments"]) + "'></parameter>\n"
        text += "    <transactions>\n"
        for transaction in self.accounts:
            text += transaction.write_transaction()
        text += "    </transactions>\n"
        text += "</firm>\n"

        return text
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_parameters_from_file
    # -------------------------------------------------------------------------
    def get_parameters_from_file(self,  firmFilename, environment):
        from xml.etree import ElementTree

        try:
            xmlText = open(firmFilename).read()
            element = ElementTree.XML(xmlText)
            self.identifier = element.attrib['identifier']

            self.parameters["rl"] = environment.static_parameters["rl"]

            # loop over all entries in the xml file
            for subelement in element:
                name = subelement.attrib['name']
                value = subelement.attrib['value']
                if (name == 'min_investments'):
                    self.parameters["min_investments"] = float(value)
                if (name == 'max_investments'):
                    self.parameters["max_investments"] = float(value)

            # self.initialize_transactions(environment)
        except:
            logging.error("    ERROR: %s could not be parsed",  firmFilename)
    # ------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_new_investments
    # -------------------------------------------------------------------------
    def get_new_investments(self, low, high):
        volume = 0.0

        from random import uniform
        volume = uniform(low, high)

        return volume
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account
    # -------------------------------------------------------------------------
    def get_account(self,  type):
        volume = 0.0

        for transaction in self.accounts:
            if (transaction.transactionType == type):
                volume = volume + float(transaction.transactionValue)

        return volume
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # get_account_num_transactions
    # -------------------------------------------------------------------------
    def get_account_num_transactions(self,  type):  # returns the number of transactions in a given account
        num_transactions = 0.0

        for transaction in self.accounts:
            if (transaction.transactionType == type):
                num_transactions += 1

        return num_transactions
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # add_transaction
    # -------------------------------------------------------------------------
    def add_transaction(self,  type,  fromID,  toID,  value,  interest,  maturity, timeOfDefault):
        from src.transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type,  fromID,  toID,  value,  interest,  maturity,  timeOfDefault)
        self.accounts.append(transaction)
        del transaction
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # clear_accounts
    # -------------------------------------------------------------------------
    def clear_accounts(self):
        self.accounts = []
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # purge_accounts
    # -------------------------------------------------------------------------
    def purge_accounts(self):
        new_accounts = []

        for transaction in self.accounts:
            if transaction.transactionValue > 0.0:
                new_accounts.append(transaction)

        self.accounts = new_accounts
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # initialize_standard_firm
    #
    # this routine initializes a firm with a standard balance sheet,
    # which can be used to make the tests more handy
    # -------------------------------------------------------------------------
    def initialize_standard_firm(self, environment):
        from src.transaction import Transaction

        self.parameters["identifier"] = "0"  # identifier
        self.parameters["rl"] = 0.05
        self.parameters["min_investments"] = -20.00  # minimum added loan demand every step
        self.parameters["max_investments"] = 20.00  # maximum added loan demand every step

        # loans - we get the first bank from the list of banks
        # if there are no banks it will be a blank which is fine for testing
        value = 250.0
        transaction = Transaction()
        transaction.this_transaction("L", environment.banks[0:1][0], self.identifier, value,  self.parameters["rl"],  0, -1)
        self.accounts.append(transaction)
        del transaction

    # -------------------------------------------------------------------------