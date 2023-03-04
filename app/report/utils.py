from services.nft import report_nft_repository


def commit_report(token_id: str):
    if not report_nft_repository.exists(token_id):
        report_nft_repository.add_token_address(token_id)
