import { useCases } from "../data/useCases";
import UseCaseItem from "./UseCaseItem";
import Card from "./Card";

export default function UseCasesList() {
  return (
    <Card>
      <h3 className="text-lg font-medium tracking-tight mb-4">Discover powerful use cases</h3>
      <div className="grid sm:grid-cols-3 gap-3">
        {useCases.map((u) => (
          <UseCaseItem key={u.id} title={u.title} cta={u.cta} />
        ))}
      </div>
    </Card>
  );
}
