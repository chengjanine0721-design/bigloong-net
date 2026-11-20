import subprocess, os

ROOT = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ROOT, ".gh_token"), "r", encoding="utf-8") as f:
    tok = f.read().strip()
url = "https://%s@github.com/chengjanine0721-design/bigloong-net.git" % tok

def run(args):
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    out = (p.stdout + p.stderr).replace(tok, "***TOKEN***")
    print("$ " + " ".join(a.replace(tok, "***TOKEN***") for a in args))
    if out.strip():
        print(out.strip())
    return p.returncode

run(["git", "add", "-A"])
rc = run(["git", "commit", "-m", "twinkle: intro + video + sheet music with PDF anchor link"])
print("commit rc=%s" % rc)
run(["git", "fetch", url, "main"])
run(["git", "rebase", "FETCH_HEAD"])
rc = run(["git", "push", url, "main"])
print("push rc=%s" % rc)
