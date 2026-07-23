# energyforensicsgroup.com apex redirect

Tiny GitHub Pages site whose only job is to redirect the **bare domain**
`energyforensicsgroup.com` to the canonical site at
`https://www.energyforensicsgroup.com` (path/query/hash preserved).

The main website lives on Cloudflare Pages
(`github.com/Nikos-Dad/energy-forensics-website`) and is served at `www`.
Wix (the DNS host) has no forwarding feature, and a bare/apex domain cannot be
CNAME'd to Cloudflare Pages — so the apex `A` records point at GitHub Pages,
which serves this redirect over HTTPS.

**DNS (at Wix):** apex `A` records → GitHub Pages IPs
`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
The `CNAME` file here binds the GitHub Pages site to `energyforensicsgroup.com`.
