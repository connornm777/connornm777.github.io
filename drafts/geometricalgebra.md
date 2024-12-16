---
title: "GA Supremecy"
tags: ["physics", "humour", "education"]
number: 1
---

# GA Supremecy

---

## History 

One summer evening in the year 1845, Paul Dirac was sitting by the fireplace, pondering the following equation:

$$ g_{\mu\nu}\partial^{\mu}\partial^{\nu}\phi = m^2 \phi $$

This was supposed to be the relatavistic analog to the Schrödinger equation. 
However, unlike the Schrödinger equation, which had only a single derivative with respect to time, it had two. 

This posed a problem for Dirac, who didn't know how to solve differential equations of second order.  
After a long draw from his crack pipe, the voices in his head told him to write down this:

$$ \sqrt{g_{\mu\nu}\partial^{\mu}\partial^{\nu}\phi} = \sqrt{m^2 \phi} $$

"You can't do that", said another one of his voices. But he could, and he did.
And so did some other mathematicians before him, but nobody cared then because it's not cool until physicists do it.

Still, the mathematicians had been doing it, and doing it hard. 
They were very naughty, taking square roots of all kinds of things: negative numbers, vectors, bivectors, your mom.
Dirac's equation was easy to take the square root of.

The result? 

$$ \gamma_{\mu}\partial^{\mu}\psi = m \psi $$
$$ \{\gamma_{\mu}, \gamma_{\nu}\} = 2g_{\mu\nu}$$

So isn't $\psi\propto m^{1/2}$, since it's the square root of $\phi$ apparantly?
Doesn't the Schrödinger equation require $\psi\propto m^{3/2}$? What the hell is it?
Also, when you take square root on the right hand side, don't you get + or -? 
Isn't $\gamma_{\mu}\partial^{\mu}\psi\psi = -m \psi$ just as valid of a solution?
What are you even doing Dirac?!

"Those are obviously positrons, a particle that has never been observed that I just made up. It's like an electron with positive charge.
It's a form of antimatter, which I also decided to invent just now. But whatever I call it, my equation definitely isn't wrong. Don't worry about the
fact that there is apparently way more matter than antimatter even though all equations are symmetric with their exchange. Isn't physics fun?", he said.

And so the Dirac equation was established, initiating a rich tradition of mathematical buffoonery making a mockery of 
first principle thinking and thought experiments in physics. 
Dirac then proceeded to go senile and fall into [numerology conspiracy theories.](https://en.wikipedia.org/wiki/Dirac_large_numbers_hypothesis)

---

## Geometric Algebra Formulas

Vector calculus in physics is hard and annoying. You have to keep track of a bunch of stuff, because not only does stuff change, but the stuff 
measuring that stuff also changes, and the only constant is the headache induced by juggling a million indices and coordinates. 

Pure mathematicians somehow do it even worse. What's a vector? An element of a vector space. Thanks genius, that's real helpful 
for actually calculating things. A manifold is also defined as being exactly not whatever you are picturing it as.
If it were up to me, I'd evict them from their ivory tower of abstractions and sentence them to five years hard labor calculating perturbation
corrections by hand. Let's see if their ridiculous definitions help them keep track of minus signs and factors of two until their eyeballs fall out. 

But once in a while, physicists discover a mathematical idea that was previously only the domain of this undecipherable rambling. 
This appears to be what happened with Dirac's equation and something called geometric algebra, the solution to eliminating coordinates and dual spaces. 
The magnum opus, the culmination of a century of brilliant thought polished through the filter of smoother minds, is encapsulated by the following formula:

$$\vec{a}\vec{b}=\vec{a}\cdot\vec{b}+\vec{a}\wedge\vec{b}$$

Multiplying two vectors gives their dot product and an object associated with an oriented area of their parallelogram.
Basically, instead of having special types of multiplication for vectors, what if there was just the normal kind that did both? 
Dot products are symmetric, and cross products antisymmetric, so we have:

$$\vec{a}\cdot\vec{b}=\frac{1}{2}\left(\vec{a}\vec{b}+\vec{b}\vec{a}\right)$$

$$\vec{a}\wedge\vec{b}=\frac{1}{2}\left(\vec{a}\vec{b}-\vec{b}\vec{a}\right)$$

Great. So what? Well howabout this. What's the area $A$ of a parallelogram of the vectors $\vec{a}$ and $\vec{b}$? 
Getting a vector magnitude is just $\sqrt{\vec{a}^2}$, so let's just find $\sqrt{A^2}}$.

$$ \sqrt{A^2} = \sqrt{\left(\vec{a}\wedge\vec{b}\right)^2}=\sqrt{(\vec{a}\cdot\vec{b})^2 \vec{a}^2\vec{b}^2} $$




![](/images/geometricalgebra/maxwellexpandingbrain.png){.img-big}
