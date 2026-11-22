# IPTV — listas organizadas

Repositório de listas M3U separadas por categoria para integração com o aplicativo.

> **SEGURANÇA: mantenha este repositório PRIVADO.** Os endereços de streaming presentes nos arquivos M3U incluem credenciais de acesso. Não publique este conteúdo em repositório público, não compartilhe os arquivos em issues/prints e não exponha o `manifest.json` junto das listas em endpoints públicos. Se as credenciais forem expostas, solicite a troca ao provedor.

## Estrutura

```text
iptv-github-repo/
├── playlists/             # Arquivos M3U independentes por categoria
├── docs/
│   └── indice_categorias.csv
├── manifest.json          # Catálogo para o aplicativo
├── scripts/
│   └── validar_m3u.py
├── .gitignore
└── README.md
```

## Integração no aplicativo

O aplicativo pode ler `manifest.json` para obter a lista de categorias, o caminho relativo de cada M3U e a quantidade de entradas. Cada arquivo em `playlists/` é independente e começa com `#EXTM3U`.

Exemplo de registro:

```json
{
  "id": "abertos",
  "name": "Abertos",
  "file": "playlists/abertos.m3u",
  "entries": 123,
  "format": "m3u"
}
```

Use os valores reais do `manifest.json`; o exemplo acima é ilustrativo.

## Validar as listas

Requer Python 3. Execute na raiz do repositório:

```bash
python scripts/validar_m3u.py
```

O validador verifica cabeçalho M3U, entradas `#EXTINF` e presença de URL após cada entrada. Ele não testa se os canais estão online.

## Atualização

Ao receber uma nova playlist de origem, gere novamente os M3U por categoria e atualize `manifest.json` e `docs/indice_categorias.csv`. Faça commit somente no repositório privado e confira as permissões antes de integrar ao app.

## Direitos e disponibilidade

Este repositório organiza os dados fornecidos; não verifica titularidade, autorização de redistribuição ou disponibilidade dos streams. Confirme que você tem autorização para usar e distribuir cada conteúdo.
