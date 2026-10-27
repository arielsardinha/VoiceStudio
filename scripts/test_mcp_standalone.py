"""
Script de teste rápido para validar a conexão e ferramentas do VoiceStudio MCP Server.
"""
import asyncio
import json
import os
import sys

# Garante UTF-8 no stdout do Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Garante que a raiz do projeto esteja no sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

async def test_mcp():
    print("=" * 60)
    print("Iniciando teste do VoiceStudio MCP...")
    print("=" * 60)

    try:
        from backend.mcp_server import create_mcp_server
        mcp = create_mcp_server()
        print("✓ Servidor FastMCP instanciado com sucesso!")
        
        tools = await mcp.list_tools()
        print(f"✓ Ferramentas registradas no MCP ({len(tools)} ferramentas):")
        for t in tools:
            desc = t.description.strip().split("\n")[0] if t.description else ""
            print(f"   - {t.name}: {desc[:65]}")

        # Teste de conexão com o backend local e protocolo MCP JSON-RPC
        print("\nVerificando conectividade e protocolo MCP em http://127.0.0.1:3900/mcp/...")
        import httpx
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                # 1. Checar health
                h = await client.get("http://127.0.0.1:3900/health")
                print(f"✓ Backend /health: status {h.status_code} ({h.text})")

                # 2. Inicialização MCP via JSON-RPC
                init_msg = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "initialize",
                    "params": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {},
                        "clientInfo": {"name": "antigravity-test", "version": "1.0.0"}
                    }
                }
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json, text/event-stream",
                    "X-OmniVoice-Client-Id": "antigravity-gemini"
                }
                mcp_res = await client.post("http://127.0.0.1:3900/mcp/", json=init_msg, headers=headers)
                print(f"✓ Resposta do MCP Initialize: status {mcp_res.status_code}")
                if mcp_res.status_code == 200:
                    sid = mcp_res.headers.get("mcp-session-id")
                    if sid:
                        print(f"✓ Sessão MCP criada: {sid}")
                        # 3. Chamar a ferramenta check_health via MCP
                        headers["mcp-session-id"] = sid
                        tool_call = {
                            "jsonrpc": "2.0",
                            "id": 2,
                            "method": "tools/call",
                            "params": {
                                "name": "check_health",
                                "arguments": {}
                            }
                        }
                        call_res = await client.post("http://127.0.0.1:3900/mcp/", json=tool_call, headers=headers)
                        print(f"✓ Chamada da ferramenta check_health (status {call_res.status_code}):")
                        for line in call_res.text.strip().split("\n"):
                            if line.startswith("data:"):
                                print(f"   {line[5:].strip()}")

                        # 4. Chamar a ferramenta list_voices via MCP
                        tool_call_voices = {
                            "jsonrpc": "2.0",
                            "id": 3,
                            "method": "tools/call",
                            "params": {
                                "name": "list_voices",
                                "arguments": {}
                            }
                        }
                        call_res2 = await client.post("http://127.0.0.1:3900/mcp/", json=tool_call_voices, headers=headers)
                        print(f"\n✓ Chamada da ferramenta list_voices (status {call_res2.status_code}):")
                        for line in call_res2.text.strip().split("\n"):
                            if line.startswith("data:"):
                                print(f"   {line[5:].strip()}")
        except Exception as e:
            print(f"ℹ Nota: Erro ao testar requisição HTTP: {e}")

    except Exception as exc:
        print(f"✗ Erro durante o teste: {exc}", file=sys.stderr)
        raise

if __name__ == "__main__":
    asyncio.run(test_mcp())
