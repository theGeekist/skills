Keep the current layout and the narrow public imports. Based on the description, the boundaries already serve their purpose: each area owns its work, while an application use case or scene coordinates the larger journey.

For a nontechnical reader, think of Checkout and Inventory as separate teams with agreed ways to ask each other for help. Asking Inventory whether stock is available does not make Inventory part of Checkout. Likewise, using the asset-library picker does not make the asset library part of the editor.

The smallest useful changes are:

- **Backend:** Keep `libs/commerce/checkout` and `libs/commerce/inventory` as peers. The `commerce` folder groups related capabilities; it need not give either one ownership of the other. Keep Checkout’s narrow stock-rule request through Inventory’s package exports, with Inventory owning the stock rule. Keep reservation-and-payment sequencing in the application use case.
- **Frontend:** Keep editor and asset-library as sibling features. The editor may use the asset-library’s public picker component when that is a narrow, natural dependency. Keep the pick-and-save workflow in the scene—the page or screen that brings the features together.
- **Enforcement:** If missing, add lint or build rules that block imports into another area’s private files while allowing its intended public exports. Avoid a blanket ban on feature-to-feature imports.
- **Migration:** Moving everything to `packages/` adds no demonstrated architectural benefit. Preserve established paths and improve boundaries as real work touches them.

Technical detail is in the backend playbook’s **Dependency rules**, **Capability grouping rule**, **Workspace mapping**, and **Incremental migration** sections, and the frontend playbook’s **Dependency rules**, **Public import guidance**, and **Boundary enforcement** sections:

- [backend-slice-architecture/SKILL.md](sandbox:/workspace/scratch/44d8812e3975/skills/skills/backend-slice-architecture/SKILL.md)
- [frontend-slice-architecture/SKILL.md](sandbox:/workspace/scratch/44d8812e3975/skills/skills/frontend-slice-architecture/SKILL.md)

Both distinguish using another area’s public interface from coordinating its workflow. A growing network of sibling dependencies deserves investigation; the two described imports alone do not justify restructuring.
