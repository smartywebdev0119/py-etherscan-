from etherscan.enums.actions_enum import ActionsEnum as actions
from etherscan.enums.fields_enum import FieldsEnum as fields
from etherscan.enums.modules_enum import ModulesEnum as modules
from etherscan.enums.tags_enum import TagsEnum as tags


class Tokens:
    @staticmethod
    def get_total_supply_by_contract_address(contract_address: str) -> str:
        """Get total supply of tokens for a contract address.

        :param contract_address: Contract address
        :type contract_address: str
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_SUPPLY}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{str}"
        )
        return url

    @staticmethod
    def get_acc_balance_by_token_and_contract_address(
        contract_address: str, address: str
    ) -> str:
        """Return ERC20 token balance for a wallet by contract/token address.

        :param contract_address: The contract/token address
        :type contract_address: str
        :param address: Wallet address
        :type address: str
        :return: The url to get
        :rtype: str
        """
        url = (
            f"{fields.MODULE}"
            f"{modules.ACCOUNT}"
            f"{fields.ACTION}"
            f"{actions.TOKEN_BALANCE}"
            f"{fields.CONTRACT_ADDRESS}"
            f"{contract_address}"
            f"{fields.ADDRESS}"
            f"{address}"
            f"{fields.TAG}"
            f"{tags.LATEST}"
        )
        return url
