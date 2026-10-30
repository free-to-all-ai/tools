# Free to All AI

**You can and must understand AI now.**

## Why "Free to All"

Three words are carved over the main entrance of the Boston Public Library: **FREE TO ALL**. Founded in 1848, it was the first large free municipal library in the United States. When its McKim Building opened in 1895, the promise went over the door. Anyone could walk in and use the most powerful information tools of the day, whoever they were and whatever they could pay. ([source](https://bpl.org/news/mckim-building-125th-anniversary))

AI is the most powerful information tool of our day. This project is that promise, rewritten for now.

## Why now

In 1974, Ted Nelson self-published *Computer Lib/Dream Machines* and told regular people that computers were too important to leave to the experts. Now the same is true of AI. The people in power are already using it. Everyone else should get to use it too.

This repo is a shelf of small, free tools for regular people. Each one does one job, gives you a checkable answer, and shows you where that answer comes from.

## The tools

| Tool | What it does | Where its answers come from |
| --- | --- | --- |
| [Michigan Renter Rights Check](renter-rights/) | Covers security deposits, eviction notices, repairs, lockouts, retaliation, and illegal lease clauses. Works out your deadlines from your dates. | Michigan Compiled Laws, checked on legislature.mi.gov on Oct 28, 2026 |
| [Insurance Denial Appeal Helper](appeal-helper/) | Works out your appeal deadlines and writes an appeal letter you can edit and send | 29 CFR 2560.503-1, 45 CFR 147.136, and Michigan's Patient's Right to Independent Review Act |
| [Detroit Medical Bill Check](bill-checker/) | Takes the codes on an itemized bill and shows what Medicare pays for each in the Detroit area. Flags duplicates and drafts a letter. | CMS 2026 Physician Fee Schedule and Clinical Lab Fee Schedule |

## How they work

- **One file each.** Every tool is a single `index.html`. Download it and open it in any browser, even offline.
- **Nothing leaves your device.** No accounts, no tracking, no servers. What you type stays on your screen.
- **Every answer cites its source.** Each card links to the law or data it came from and is labeled by how sure it is: what the law says directly, what depends on your facts, and when to get help now.
- **Information, not advice.** These tools explain your rights and the rules. They are not a lawyer, a doctor, or a tax preparer.

## Keeping them current

Laws and rates change. Every tool lists the date its sources were checked. The bill checker's rates come from CMS and change every January. To rebuild it, see `bill-checker/make.py`.

## Add your own

Have a tool that helps people and has a checkable right answer? Open an issue or a pull request. The bar is simple: it cites its sources, it doesn't track anyone, and it tells people when they need a real professional.

## License

MIT. Free to all.
