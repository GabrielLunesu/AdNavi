import Card from "./Card";
import KeyValue from "./KeyValue";
import { company } from "../data/company";

export default function CompanyCard() {
  return (
    <Card className="mb-8">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium tracking-tight">Company</h3>
        <button className="text-sm text-cyan-400 hover:text-cyan-300">Edit Company Info</button>
      </div>
      <div className="grid sm:grid-cols-2 gap-4">
        <div className="space-y-2">
          <KeyValue label="Name">{company.name}</KeyValue>
          <KeyValue label="Industry">{company.industry}</KeyValue>
        </div>
        <div className="space-y-2">
          <KeyValue label="Website">
            <a className="text-cyan-400 hover:text-cyan-300" href="#">{company.website}</a>
          </KeyValue>
          <KeyValue label="Tagline">{company.tagline}</KeyValue>
        </div>
      </div>
    </Card>
  );
}
