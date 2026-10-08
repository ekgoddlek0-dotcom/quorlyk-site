# DNS 가 깃허브로 바뀔 때까지 기다렸다가 → 페이지 확인 → https 강제 → 텔레그램 알림. 최대 48시간.
import subprocess, time, json, io, os, urllib.request
R = "ekgoddlek0-dotcom/quorlyk-site"
def ip():
    out = subprocess.run(["nslookup", "quorlyk.com", "8.8.8.8"], capture_output=True, text=True, errors="replace").stdout
    return [l.split(":")[-1].strip() for l in out.splitlines()[3:] if "185.199." in l]
def gh(*a):
    return subprocess.run(["gh", "api", *a], capture_output=True, text=True, errors="replace")
def tell(msg):
    p = r"C:\비지니스\sns공장\알림.txt"; io.open(p, "w", encoding="utf-8").write(msg)
    subprocess.run(["python", "notify.py", p], cwd=r"C:\비지니스\company_control", capture_output=True)
t0 = time.time(); stage = "dns"
while time.time() - t0 < 48 * 3600:
    if stage == "dns" and ip():
        stage = "https"; print("DNS OK", ip(), flush=True)
    if stage == "https":
        r = gh("-X", "PUT", f"repos/{R}/pages", "-F", "https_enforced=true")
        if r.returncode == 0:
            try:
                ok = urllib.request.urlopen("https://quorlyk.com/", timeout=30).status == 200
            except Exception as e:
                ok = False; print("https 아직", type(e).__name__, flush=True)
            if ok:
                print("DONE https", flush=True)
                tell("✅ quorlyk.com 새 사이트 연결 완료 (https). https://quorlyk.com")
                break
        else:
            print("인증서 대기", r.stderr[-120:], flush=True)
    time.sleep(120)
