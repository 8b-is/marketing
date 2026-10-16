#!/usr/bin/env bash
# invite-members.sh — Ensure 8bit-wraith, poo757/poe757, and standardgalactic
# have full member + admin collaborator access to 8b-is and 8b-is/marketing.
set -euo pipefail

ORG="8b-is"
REPO="8b-is/marketing"
MEMBERS=("8bit-wraith" "poo757" "poe757" "standardgalactic")

echo "=== Granting triangle team admin on $REPO ==="
gh api --method PUT "/orgs/$ORG/teams/triangle/repos/$REPO" -f permission=admin || true

for u in "${MEMBERS[@]}"; do
  echo "=== Checking GitHub user: $u ==="
  if ! gh api "/users/$u" >/dev/null 2>&1; then
    echo "  · user '$u' not found on GitHub (skipping)"
    continue
  fi
  echo "  → inviting/updating org membership for $u in $ORG..."
  gh api --method PUT "/orgs/$ORG/memberships/$u" -f role=member \
    --jq '"  ✓ org membership: " + .state + " (" + .role + ")"' || true

  echo "  → granting admin permission on $REPO to $u..."
  gh api --method PUT "/repos/$REPO/collaborators/$u" -f permission=admin >/dev/null 2>&1 \
    && echo "  ✓ repo admin granted to $u" || true
done
