import OpportunityItem from "./OpportunityItem";

export default function OpportunityRadar({ items }) {
  return (
    <section className="mb-6">
      <h3 className="text-xl font-medium mb-3">Opportunity Radar</h3>
      <div className="space-y-3">
        {items?.map((o, idx) => (
          <OpportunityItem key={idx} {...o} />
        ))}
      </div>
    </section>
  );
}
