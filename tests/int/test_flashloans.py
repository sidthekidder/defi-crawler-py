from deficrawler.lending import Lending


def test_flashloans_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    flash_loans = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 18:01:00', "flashloans")

    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Ethereum")
    assert(flash_loans[0]['version'] == 2)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)


def test_flashloans_aave_2_avalanche():
    aave = Lending(protocol="Aave", chain="Avalanche", version=2)
    flash_loans = aave.get_data_from_date_range(
        '10/10/2021 00:00:01', '18/10/2021 18:01:00', "flashloans")

    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Avalanche")
    assert(flash_loans[0]['version'] == 2)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)


def test_flashloans_aave_2_eth_user():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    flash_loans = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 18:01:00', "flashloans", "0x4f2769e87c7d96ed9ca72084845ee05e7de5dda2")

    for flash_loan in flash_loans:
        assert(flash_loan['user'] ==
               "0x4f2769e87c7d96ed9ca72084845ee05e7de5dda2")


def test_flashloans_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    flash_loans = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 18:01:00', "flashloans")
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Polygon")
    assert(flash_loans[0]['version'] == 2)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)


def test_flashloans_aave_2_polygon_user():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    flash_loans = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 18:01:00', "flashloans", "0xabcd3c5e8aed3b8d8096f0f33c7aa1cb5d555dfb")

    for flash_loan in flash_loans:
        assert(flash_loan['user'] ==
               "0xabcd3c5e8aed3b8d8096f0f33c7aa1cb5d555dfb")


def test_flashloans_aave_3_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=3)
    flash_loans = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 18:01:00', "flashloans")
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Polygon")
    assert(flash_loans[0]['version'] == 3)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)

def test_flashloans_aave_3_arbitrum():
    aave = Lending(protocol="Aave", chain="Arbitrum", version=3)
    flash_loans = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 18:01:00', "flashloans")
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Arbitrum")
    assert(flash_loans[0]['version'] == 3)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)


def test_flashloans_aave_3_optimism():
    aave = Lending(protocol="Aave", chain="Optimism", version=3)
    flash_loans = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 18:01:00', "flashloans")
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Optimism")
    assert(flash_loans[0]['version'] == 3)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)


def test_flashloans_aave_3_fantom():
    aave = Lending(protocol="Aave", chain="Fantom", version=3)
    flash_loans = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 18:01:00', "flashloans")
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Fantom")
    assert(flash_loans[0]['version'] == 3)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)


def test_flashloans_aave_3_avalanche():
    aave = Lending(protocol="Aave", chain="Avalanche", version=3)
    flash_loans = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 18:01:00', "flashloans")
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Avalanche")
    assert(flash_loans[0]['version'] == 3)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)