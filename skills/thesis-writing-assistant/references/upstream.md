# Προέλευση και προσαρμογή

Το skill συνδυάζει τις απαιτήσεις του συγγραφέα με επιλεγμένες ιδέες από δύο
εργαλειοθήκες. Οι παρακάτω πηγές μελετήθηκαν στις 2026-11-21.

## Κύρια βάση: Claude Scholar

[Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar):

- [ml-paper-writing](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/ml-paper-writing/SKILL.md): σύνθεση από πραγματικό research repo και claim ledger.
- [results-analysis](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/results-analysis/SKILL.md): μονάδα ανάλυσης, προέλευση, αβεβαιότητα και επιτρεπτή ισχύς ισχυρισμών.
- [results-report](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/results-report/SKILL.md): συνεκτική ερμηνεία ευρημάτων και σχημάτων.
- [paper-self-review](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/paper-self-review/SKILL.md): έλεγχος υποστήριξης συμπερασμάτων και υπερβολικών διατυπώσεων.
- [citation-workflow](https://github.com/Galaxy-Dawn/claude-scholar/blob/main/skills/ml-paper-writing/references/citation-workflow.md): ξεχωριστή επαλήθευση μεταδεδομένων και συγκεκριμένου ισχυρισμού στην πηγή.

Η άδεια MIT διατηρείται στο
[CLAUDE_SCHOLAR_LICENSE](../CLAUDE_SCHOLAR_LICENSE).
Η προσαρμογή δεν εγκαθιστά την εργαλειοθήκη ούτε εξαρτάται από αυτή στο runtime.
Δεν μεταφέρει γενικούς αυτοματισμούς, agents, hooks, global settings ή ανάγκη
για Obsidian/Zotero. Το skill συνεργάζεται με τα ήδη υπάρχοντα thesis skills.

Δεν υιοθετούνται τα conference templates και οι καθολικές απαιτήσεις για
συγκεκριμένα reports ή στατιστικούς ελέγχους σε κάθε ενότητα. Η απαιτούμενη
πληροφορία μπορεί να τεκμηριώνεται στα υπάρχοντα CSV/notebooks και στο context.
Το project-specific πρωτόκολλο repeated/grouped CV ελέγχεται στον πραγματικό
κώδικα, αντί να αντικαθίσταται από ένα γενικό δέντρο επιλογής tests.
Δεν θεωρείται επαλήθευση ισχυρισμού η απλή παρουσία λέξης-κλειδιού στο abstract.

## Συμπληρωματική βάση: Academic Paper Skills

[lishix520/academic-paper-skills](https://github.com/lishix520/academic-paper-skills):

- [strategist/SKILL.md](https://github.com/lishix520/academic-paper-skills/blob/main/strategist/SKILL.md)
- [composer/SKILL.md](https://github.com/lishix520/academic-paper-skills/blob/main/composer/SKILL.md)
- [LICENSE](https://github.com/lishix520/academic-paper-skills/blob/main/LICENSE)

Οι σύνδεσμοι αφορούν το μεταβαλλόμενο branch `main`, όχι pinned commit.
Η άδεια MIT του upstream διατηρείται στο [UPSTREAM_LICENSE](../UPSTREAM_LICENSE).
Η αναφορά αυτή αφορά τα εργαλεία συγγραφής, όχι βιβλιογραφική τεκμηρίωση των
επιστημονικών συμπερασμάτων της εργασίας.

## Τι αξιοποιείται

- Από το Strategist: σύνδεση ερευνητικού ερωτήματος με τεκμήρια, πλάνο ενότητας
  και κριτική εξέταση επάρκειας επιχειρημάτων.
- Από το Composer: συγγραφή βάσει πλάνου, έλεγχος συνοχής, αναθεώρηση και
  διακριτή καταγραφή προβλημάτων που επηρεάζουν το κείμενο.

## Τι αλλάζει για τη συγκεκριμένη διπλωματική

- Το σημείο αναφοράς γίνεται ο Άξονας, η πραγματική μεθοδολογία και οι οδηγίες
  σχολής/επιβλέποντα όταν δοθούν, αντί για επιλογή preprint platform.
- Η ερμηνεία στηρίζεται σε συγκεκριμένα υπάρχοντα artifacts ML/PM, με έλεγχο
  μονάδων, αβεβαιότητας, συγκρισιμότητας και προέλευσης.
- Η ανθρώπινη κρίση παραμένει στον συγγραφέα. Δεν επιβάλλονται παύσεις
  έγκρισης σε κάθε κεφάλαιο ούτε γίνονται μεθοδολογικές αλλαγές σιωπηλά.
- Δεν μεταφέρονται quotas πηγών, αυτοβαθμολογήσεις τύπου 28/35, ποσοστά
  «πρωτοτυπίας», προβλέψεις impact ή υπόσχεση submission-ready manuscript.
- Δεν αντιγράφονται/εκτελούνται τα upstream Python scripts και δεν απαιτούνται
  Exa/Tavily ή η εγκατάσταση των δύο upstream skills.

Η τυπική διάταξη project skill στο Claude Code επαληθεύτηκε στην
[επίσημη τεκμηρίωση](https://code.claude.com/docs/en/skills).
