# Free to All AI

**You can and must understand AI now.**

**Use the tools here: [free-to-all-ai.github.io/tools](https://free-to-all-ai.github.io/tools/)**

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
| [Gig Driver True Pay Calculator](gig-pay/) | Takes the pay, hours, and miles from your rideshare or delivery app and shows what you really made per hour after car costs. Shows unpaid miles and hours, a tax set-aside, and whether an offer is worth taking. | IRS standard mileage rates (Notice 2026-10 and Announcement 2026-11), IRS self-employment tax rules, and Michigan's minimum wage law, checked Oct 30, 2026 |
| [Benefits Cut Letter Deadlines](benefits-deadlines/) | For a Michigan letter that denies, lowers, or stops food assistance (SNAP), Medicaid, cash, or child care help. Works out the last day to ask for a hearing and keep your benefits while you wait, and the last day to ask at all. Drafts the hearing request. | MDHHS Bridges Administrative Manual (BAM 600, 220, and 210), 7 CFR 273.15, and 42 CFR 431, checked Oct 30, 2026 |
| [Michigan Back Pay Check](back-pay/) | Shows Michigan's minimum wage by date. Takes your hours and pay week by week and works out unpaid minimum wage, overtime, and promised pay, plus your filing deadlines. Gives a summary to paste into the state's free wage claim and the steps to file it. | Michigan's Improved Workforce Opportunity Wage Act (MCL 408.934 to 408.939), Payment of Wages Act (MCL 408.481 to 408.488), and the state labor department's rate history and claim form, checked Oct 30, 2026 |
| [Detroit HOPE Property Tax Exemption Check](hope-exemption/) | For Detroit homeowners. Takes household size, income, and savings and shows whether you likely qualify for a full or partial HOPE property tax exemption on the city's 2026 table. Gives the November 6, 2026 deadline, what to bring, how to apply, and the note that only the Board of Review decides. | The City of Detroit's 2026 HOPE page and application, and MCL 211.7u (Michigan's poverty exemption law), checked Oct 31, 2026 |
| [Michigan Winter Shutoff Protection Check](shutoff-protection/) | For a Michigan gas or electric bill you're behind on, or a shut off notice. Shows whether the Winter Protection Plan (Nov 1 to Mar 31), senior protection, a medical hold, critical care, or military protection covers you, about what you'd pay each month to stay on, and whether your notice gave you the required 10 days. Covers state-regulated utilities like DTE and Consumers Energy, and flags where city utilities and co-ops differ. Writes a script for the call. | MPSC consumer standards (Mich. Admin. Code R 460.101 to 460.169), MCL 460.9c, 460.9q, 460.9r, 460.9s, and 460.36, and the 2026 HHS poverty guidelines, checked Oct 31, 2026 |
| [Michigan Clean Slate Expungement Check](clean-slate/) | List your Michigan convictions and dates. Shows whether each one may clear automatically under Clean Slate and when, or whether you may be able to apply to the court to set it aside (expunge it) and the earliest date. Covers the limits on felonies and assaultive crimes, the one-incident rule, first OWI, marijuana, and convictions that can never be cleared. Gives the steps to apply, a summary to bring to free legal help, and where to find that help. | Michigan's set aside law (MCL 780.621 to 780.624, including the 2020 Clean Slate amendments), the State Police and Attorney General expungement pages, and court form MC 227, checked Oct 31, 2026 |

## How they work

- **One file each.** Every tool is a single `index.html`. Download it and open it in any browser, even offline.
- **Nothing leaves your device.** No accounts, no tracking, no servers. What you type stays on your screen.
- **Every answer cites its source.** Each card links to the law or data it came from and is labeled by how sure it is: what the law says directly, what depends on your facts, and when to get help now.
- **Information, not advice.** These tools explain your rights and the rules. They are not a lawyer, a doctor, or a tax preparer.

## Keeping them current

Laws and rates change. Every tool lists the date its sources were checked. The bill checker's rates come from CMS and change every January. To rebuild it, see `bill-checker/make.py`. The gig pay calculator's IRS mileage rates live in a short table near the top of its script. The IRS usually sets next year's rate in December. The shutoff check's poverty guideline numbers sit at the top of its script. HHS publishes new ones each January.

## Add your own

Have a tool that helps people and has a checkable right answer? Open an issue or a pull request. The bar is simple: it cites its sources, it doesn't track anyone, and it tells people when they need a real professional.

So people can find a new tool: give its page a plain-language `<title>` and description in the words people actually search for, add a card to the homepage (`index.html`), add its address to `sitemap.xml`, and add a 1200 by 630 link-preview image in `og/`.

## License

MIT. Free to all.
