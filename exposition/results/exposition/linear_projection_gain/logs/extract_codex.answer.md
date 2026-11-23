Throughout, for a scale $\delta\in(0,1)$, a loss exponent $\epsilon>0$ and a support radius $R\ge0$, we say that a pair $(\mu,\nu)$ \emph{satisfies the hypotheses at scale $\delta$ with loss $\epsilon$ and radius $R$} if $\mu(\R^{k+1})\le1$, $\nu(S^k)\le1$, $|x|\le R$ for $\mu$-a.e.\ $x$, $\mu(B(x,r))\le\delta^{-\epsilon}r^t$ and $\nu(B(w,r))\le\delta^{-\epsilon}r^q$ for all centers and all $\delta\le r\le1$, and, when $q=k-1$, the plate bound \eqref{ang:endpoint-plate} holds for every linear hyperplane $H$ and all $\delta\le r\le1$. A relation $E$ \emph{has the fiber cover at scale $\delta$ with loss $\epsilon$} if for every $w\in S^k$ there is a finite set $A_w\subset\R^{k+1}$ with $\#A_w\le\delta^{-q-\epsilon}$ such that every $x\in E_w$ satisfies $|P_{w^\perp}(x-a)|\le C\delta$ for some $a\in A_w$. This property clearly passes to subsets of $E$.

\begin{lemma}[Normalized dyadic gain]\label{lpg:unit}
Let $k,q,t,C,\zeta$ be as in the theorem. There are $\epsilon,c,d>0$ such that for every $N$ with $\delta=2^{-N}<d$, every pair $(\mu,\nu)$ satisfying the hypotheses at scale $\delta$ with loss $\epsilon$ and radius $\tfrac14$, and every measurable $E$ with $|x|\le\tfrac14$ for all $(x,w)\in E$ and the fiber cover at scale $\delta$ with loss $\epsilon$, we have $(\mu\otimes\nu)(E)\le\delta^c$.
\end{lemma}

This normalized estimate is taken from earlier work and is obtained in two regimes, writing $k=h+2$. In the endpoint case $q=k-1$ it follows from the endpoint angular gain estimate, after observing that the slab of directions within $r$ of a hyperplane is contained in the plate of \eqref{ang:endpoint-plate}. In the case $q>k-1$ it follows from the non-endpoint dyadic tube gain estimate, which is driven by the planar discretized Furstenberg estimate (Theorem~\ref{ang:furstenberg}). In both regimes the ball bounds are only needed at the dyadic radii $2^{-j}$, $j\le N$. The width condition $|P_{w^\perp}(x-a)|\le C\delta$ is the same as $|(x-a)-\langle w,x-a\rangle w|\le C\delta$.

We also use two elementary facts.

\emph{(a) Absorbing constants.} For $M\ge0$ and $c>0$ there is $d>0$ with $M\delta^c\le\delta^{c/2}$ for $0<\delta<d$. Indeed, $M\delta^{c/2}\to0$, so $M\delta^{c/2}<1$ for small $\delta$. Multiplying by $\delta^{c/2}$ gives the claim.

\emph{(b) Rounding the scale.} Let $\epsilon<\eta$ and $p+\eta\ge0$. Then there is $d>0$ such that $\delta^{-p-\epsilon}\le u^{-p-\eta}$ whenever $0<\delta<d$ and $0<u\le2\delta$. Indeed, choose $d$ so that $\delta^{\eta-\epsilon}\le2^{-p-\eta}$ for $\delta<d$. Then
\[
\delta^{-p-\epsilon}=\delta^{-p-\eta}\delta^{\eta-\epsilon}\le(2\delta)^{-p-\eta}\le u^{-p-\eta},
\]
where the last step uses $u\le2\delta$ and $-p-\eta\le0$.

\begin{proof}
Fix $k,q,t,C,\zeta$ as in the theorem. Fix also a radius $R\ge0$ such that all point measures are supported in $\{|x|\le R\}$. Note that $q\ge k-1\ge1>0$.

\emph{Step 1: bounded support at dyadic scales.} Let $\epsilon,c,d$ be given by Lemma~\ref{lpg:unit}. The closed ball $\overline B(0,R)$ is compact. Hence it is covered by finitely many open balls $B(b,\tfrac14)$ with $b\in\mathcal B$, where $\mathcal B$ is a finite set. By (a), choose $d'>0$ with $\#\mathcal B\cdot\delta^c\le\delta^{c/2}$ for $\delta<d'$.

Let $\delta=2^{-N}<\min(d,d')$. Let $(\mu,\nu)$ satisfy the hypotheses at scale $\delta$ with loss $\epsilon$ and radius $R$. Let $E$ be measurable for the completed product measure and have the fiber cover at scale $\delta$ with loss $\epsilon$. Choose a measurable $E_0\subset E$ with $E_0=E$ up to a $\mu\otimes\nu$-null set. Put
\[
F=E_0\cap\{(x,w):|x|\le R\}.
\]
Since $\mu$ is carried by $\{|x|\le R\}$, we have $(\mu\otimes\nu)(F)=(\mu\otimes\nu)(E)$. Moreover $F\subset E$, so $F$ inherits the fiber cover.

For $b\in\mathcal B$, put $P_b=F\cap\{(x,w):|x-b|\le\tfrac14\}$. Let $\mu_b$ be the pushforward of $\mu|_{\overline B(b,1/4)}$ under $x\mapsto x-b$. Let
\[
E_b=\{(x,w):(x+b,w)\in P_b\}.
\]
We check the hypotheses of Lemma~\ref{lpg:unit} for $\mu_b$, $\nu$ and $E_b$.
\begin{itemize}
\item The measure $\mu_b$ has total mass at most $\mu(\R^{k+1})\le1$, and it is carried by $\overline B(0,\tfrac14)$.
\item We have $\mu_b(B(x,r))\le\mu(B(x+b,r))\le\delta^{-\epsilon}r^t$.
\item The direction measure $\nu$ and its bounds are unchanged.
\item The set $E_b$ is measurable, and $|x|\le\tfrac14$ for every $(x,w)\in E_b$.
\item If $A_w$ is a tube cover for $F_w$, then $A_w-b$ covers $(E_b)_w$ with the same width and at most as many anchors.
\end{itemize}
Translation preserves product mass, so $(\mu_b\otimes\nu)(E_b)=(\mu\otimes\nu)(P_b)$. Lemma~\ref{lpg:unit} therefore gives $(\mu\otimes\nu)(P_b)\le\delta^c$.

Every point of $F$ has $|x|\le R$, so it lies in some $B(b,\tfrac14)$. Hence $F\subset\bigcup_{b\in\mathcal B}P_b$, and
\[
(\mu\otimes\nu)(E)=(\mu\otimes\nu)(F)\le\sum_{b\in\mathcal B}(\mu\otimes\nu)(P_b)\le\#\mathcal B\,\delta^c\le\delta^{c/2}.
\]
Rename $c/2$ as $c$ and $\min(d,d')$ as $\delta_0$. This proves the theorem for dyadic $\delta=2^{-N}<\delta_0$ with loss $\epsilon$, without assuming bounded support of $E$ and without localizing directions. In particular, it holds when all directions of $E$ lie in a cap of radius $\rho=1$ about some $w_0$.

\emph{Step 2: arbitrary scales.} Let $\eta,c,\delta_0$ be as obtained in Step 1. Apply (b) twice with loss gap $\eta/2<\eta$: once with $p=0$, giving a threshold $d_1$, and once with $p=q$, giving a threshold $d_2$. By (a), choose $d_3$ with $2^c\delta^c\le\delta^{c/2}$ for $\delta<d_3$. Set
\[
d=\min(1,\delta_0/2,d_1,d_2,d_3),\qquad \epsilon=\eta/2.
\]
Let $0<\delta<d$, and let $(\mu,\nu,E)$ satisfy the hypotheses at scale $\delta$ with loss $\eta/2$. Choose $N$ with $2^{-N-1}<\delta\le2^{-N}=:u$. Then $\delta\le u\le2\delta$, and $u<\delta_0$.
\begin{itemize}
\item By (b) with $p=0$, we have $\delta^{-\eta/2}\le u^{-\eta}$. The radii $u\le r\le1$ lie in $[\delta,1]$. So the ball bounds and the plate bound at scale $\delta$ with loss $\eta/2$ give the same bounds at scale $u$ with loss $\eta$.
\item By (b) with $p=q$, each anchor set satisfies $\#A_w\le\delta^{-q-\eta/2}\le u^{-q-\eta}$.
\item The width satisfies $C\delta\le Cu$.
\end{itemize}
Thus $(\mu,\nu,E)$ satisfies the hypotheses at the dyadic scale $u$ with loss $\eta$, and Step 1 gives
\[
(\mu\otimes\nu)(E)\le u^c\le2^c\delta^c\le\delta^{c/2}.
\]
This bound holds for every relation $E$ whose directions lie in a cap of radius $\rho=1$.

\emph{Step 3: removing the cap localization.} Let $\rho$, $\epsilon$, $c$ and $\delta_0$ be the constants from Step 2, so that the estimate holds for relations whose directions lie within $\rho$ of a fixed $w_0$. The sphere $S^k$ is compact, so it is covered by finitely many open caps $B(a,\rho)$ with $a\in\mathcal A$, where $\mathcal A$ is a finite set. By (a), choose $d$ with $\#\mathcal A\cdot\delta^c\le\delta^{c/2}$ for $\delta<d$.

Let $\delta<\min(\delta_0,d)$, and let $(\mu,\nu,E)$ satisfy the hypotheses of the theorem. For $a\in\mathcal A$, put
\[
F_a=E\cap\{(x,w):w\in B(a,\rho)\}.
\]
Each $F_a$ is measurable for the completed product measure, has the fiber cover because it is a subset of $E$, and has all its directions within $\rho$ of $a$. Step 2 therefore gives $(\mu\otimes\nu)(F_a)\le\delta^c$. Since $E\subset\bigcup_{a\in\mathcal A}F_a$,
\[
(\mu\otimes\nu)(E)\le\sum_{a\in\mathcal A}(\mu\otimes\nu)(F_a)\le\#\mathcal A\,\delta^c\le\delta^{c/2}.
\]
This is the claim, with loss $\epsilon$, gain $c/2$ and scale threshold $\min(\delta_0,d)$. These constants depend only on $k,q,t,C,R,\zeta$.
\end{proof}
