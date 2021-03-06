#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

"""
This is a minimal example.

black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2012 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>

The development of this software has been supported by the ERA-Net
on Complexity through the grant RESINEE.
"""

# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':
    import pdb  # python debugger, for debugging purposes only

    import sys
    # sys.path.append('src/')
    import logging

    from tests.tests_bank import TestsBank
    from tests.tests_central_bank import TestsCentralBank
    from tests.tests_environment import TestsEnvironment
    from tests.tests_firm import TestsFirm
    from tests.tests_helper import TestsHelper
    from tests.tests_household import TestsHousehold
    from tests.tests_market import TestsMarket
    from tests.tests_measurement import TestsMeasurement
    from tests.tests_runner import TestsRunner
    from tests.tests_shock import TestsShock
    from tests.tests_transaction import TestsTransaction
    from tests.tests_updater import TestsUpdater

    test_bank = TestsBank()
    test_central_bank = TestsCentralBank()
    test_environment = TestsEnvironment()
    test_firm = TestsFirm()
    test_helper = TestsHelper()
    test_household = TestsHousehold()
    test_market = TestsMarket()
    test_measurement = TestsMeasurement()
    test_runner = TestsRunner()
    test_shock = TestsShock()
    test_transaction = TestsTransaction()
    test_updater = TestsUpdater()

    # Tests for Bank
    test_bank.bank__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__get_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__set_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__get_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__set_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__get_parameters_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__check_consistency(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__get_account(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__get_account_num_transactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__initialize_standard_bank(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__get_transactions_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_bank.bank__getattr(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for CentralBank
    test_central_bank.central_bank__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__get_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__set_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__get_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__set_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__get_parameters_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__check_consistency(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__get_account(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__get_account_num_transactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__get_transactions_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_central_bank.central_bank__getattr(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Firm
    test_firm.firm__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__get_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__set_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__get_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__set_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__get_parameters_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__get_account(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__get_account_num_transactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__initialize_standard_firm(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__get_transactions_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_firm.firm__getattr(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Household
    test_household.household__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__get_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__set_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__get_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__set_state_variables(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__get_parameters_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__get_account(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__get_account_num_transactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__initialize_standard_household(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__get_transactions_from_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_household.household__getattr(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Environment
    test_environment.environment__add_static_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__add_variable_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__get_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__set_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__get_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__set_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__get_assets(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__set_assets(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__get_shocks(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__set_shocks(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__add_shock(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__print_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__write_environment_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__read_xml_config_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__initialize(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__initialize_banks_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__initialize_firms_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__initialize_households_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__initialize_central_bank_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__get_agent_by_id(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__read_transactions_for_banks(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__read_transactions_for_firms(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__read_transactions_for_households(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__read_transactions_for_central_bank(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__check_global_transaction_balance(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__check_agent_homogeneity(["tests/environments/", "test_all_methods", "tests/log/"])
    test_environment.environment__update_asset_returns(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Transaction
    test_transaction.transaction__init(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__del(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_type_(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_type_(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_asset(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_asset(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_from_(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_from_(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_to(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_to(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_amount(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_amount(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_interest(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_interest(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_maturity(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_maturity(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__get_time_of_default(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__set_time_of_default(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__this_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__remove_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__print_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__write_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
    test_transaction.transaction__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Helper
    test_helper.helper__initialize_standard_bank(["tests/environments/", "test_all_methods", "tests/log/"])
    test_helper.helper__initialize_standard_firm(["tests/environments/", "test_all_methods", "tests/log/"])
    test_helper.helper__initialize_standard_household(["tests/environments/", "test_all_methods", "tests/log/"])
    test_helper.helper__cobb_douglas(["tests/environments/", "test_all_methods", "tests/log/"])
    test_helper.helper__leontief(["tests/environments/", "test_all_methods", "tests/log/"])
    test_helper.helper__ces(["tests/environments/", "test_all_methods", "tests/log/"])
    test_helper.helper__translog(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Market
    test_market.market__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__get_tolerance(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__set_tolerance(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__get_resolution(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__set_resolution(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__get_amplification(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__set_amplification(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__tatonnement(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__rationing(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__rationing_proportional(["tests/environments/", "test_all_methods", "tests/log/"])
    test_market.market__rationing_abstract(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Measurement
    test_measurement.measurement__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__get_config(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__set_config(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__get_environment(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__set_environment(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__get_runner(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__set_runner(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__get_filename(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__set_filename(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__get_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__set_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__get_csv_writer(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__set_csv_writer(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__init(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__open_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__write_to_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__close_file(["tests/environments/", "test_all_methods", "tests/log/"])
    test_measurement.measurement__read_xml_config_file(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Runner << TINA TO WRITE
    test_runner.runner__init__(["tests/environments/", "test_all_methods", "tests/log/"])
    test_runner.runner__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_runner.runner__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_runner.runner__get_num_sweeps(["tests/environments/", "test_all_methods", "tests/log/"])
    test_runner.runner__set_num_sweeps(["tests/environments/", "test_all_methods", "tests/log/"])
    test_runner.runner__do_run(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Shock
    test_shock.shock__do_shock(["tests/environments/", "test_all_methods", "tests/log/"])

    # Tests for Updater
    test_updater.updater__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__get_model_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__set_model_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__get_interactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__set_interactions(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__str(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__init(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__accrue_interests(["tests/environments/", "test_all_methods", "tests/log/"])
    # test_updater.updater__endow_labour(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__sell_labour(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__consume_rationed(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__net_loans_deposits(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__remove_perishable(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__capitalise(["tests/environments/", "test_all_methods", "tests/log/"])
    test_updater.updater__do_update(["tests/environments/", "test_all_methods", "tests/log/"])
