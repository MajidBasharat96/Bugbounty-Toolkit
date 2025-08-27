from recon.subenum import check_subdomain
def test_check():
    # network calls are not run in CI; ensure function returns None for unreachable
    assert check_subdomain('nonexistent.invalid','nope') in (None,)
