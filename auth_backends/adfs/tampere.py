import uuid

from auth_backends.adfs.base import BaseADFS


class TampereADFS(BaseADFS):
    """Tampere ADFS authentication backend"""
    name = 'tampere_adfs'
    AUTHORIZATION_URL = 'https://sts.tampereenseutu.fi/adfs/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://sts.tampereenseutu.fi/adfs/oauth2/token'

    resource = 'https://auth.tampere.fi/adfs'
    domain_uuid = uuid.UUID('405f4629-a825-4d2b-b1e8-e7702f291e1c')
    realm = 'tampere'
    cert = (
        'MIIDaTCCAlGgAwIBAgIBATANBgkqhkiG9w0BAQsFADAvMS0wKwYDVQQDEyRBREZT'
        'IFNpZ25pbmcgLSBzdHMudGFtcGVyZWVuc2V1dHUuZmkwHhcNMTYwNTIzMTA0MjAw'
        'WhcNMjEwNTIzMTA0MjAwWjAvMS0wKwYDVQQDEyRBREZTIFNpZ25pbmcgLSBzdHMu'
        'dGFtcGVyZWVuc2V1dHUuZmkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB'
        'AQDBcHZCVOOPGBRTxGYj5LbqPx82zBKyaQ23bTUnlyzvtGgvFs1D6qO7+/JxDGz+'
        'WnK13KOaLhPxBGgB0Owml8VsisotGqXamCHH9hkQQ0h/rF3YtIfaBj1deC+NujdC'
        'bB6ArSZoOM9A1RftrvZ7woivxqb5Tt827Xus+AA6MnvTU/odPEzPTlJ24clk1veG'
        'CpLAcUL5/2HG5ebeL8ixTGtTmJSf0kSoPmq5PwGnadYIGJfsY8xSzzMailWM+kcL'
        'A8gToJJdLABAD4hjdYkXT5Uib3w6jx1mFN4fLd0XrOSUJtNke0kcI0RXuBxw+/47'
        'LAFm5mK9yhlwGu1MuhCTWnwRAgMBAAGjgY8wgYwwDAYDVR0TAQH/BAIwADAdBgNV'
        'HQ4EFgQUdCipMYyoCMrQwAmtbiKgxmSIFpgwCwYDVR0PBAQDAgSwMB0GA1UdJQQW'
        'MBQGCCsGAQUFBwMBBggrBgEFBQcDAjARBglghkgBhvhCAQEEBAMCBkAwHgYJYIZI'
        'AYb4QgENBBEWD3hjYSBjZXJ0aWZpY2F0ZTANBgkqhkiG9w0BAQsFAAOCAQEAWrJv'
        'xHJKaiFu/cDMPDkzZuojXhnKaK9I1IYc5i9lf95B8ixlg86ntpfxzE6c47T6hbkY'
        '//iOdbVZM9eYP4XPt01bXxkfZ45oQZyjtBnmauxq87ModBMDrZ7mYOodgBTXlxW9'
        'NCirC7fdC5sC2NcqP8awlOr1kw0xroLnCBAWlGy2y10nLcKk8xmUceiAzTk9zTp5'
        'HK1BovEtxjfzrgvl6p6DH+ik90guj2jgHNxw+qM2I6QjCa0g5wPqgKSgKxIhlbNe'
        'iaGjZUWr1pxBKWiPzx3qVqdNRgAWkC1MBd0o+e+QZqsDqrCtGBLFFRQqpqLPw1PO'
        'caxCehYF/xwqhHys0Q=='
    )

    def clean_attributes(self, attrs_in):
        attr_map = {
            'primarysid': 'primary_sid',
            'given_name': 'first_name',
            'family_name': 'last_name',
            'email': 'email',
        }

        # Convert attribute names to lowercase
        attrs_in = {k.lower(): v for k, v in attrs_in.items()}

        attrs = {}
        for in_name, out_name in attr_map.items():
            val = attrs_in.get(in_name, None)
            if val is not None:
                if out_name in ('department_name', 'email', 'username'):
                    val = val.lower()
                attrs[out_name] = val
            attrs[out_name] = val

        return attrs
